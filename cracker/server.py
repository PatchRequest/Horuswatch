from socketserver import ThreadingMixIn
from flask import Flask
from flask import request
from flask_cors import CORS
import subprocess
import os
import re
from threading import Thread

app = Flask(__name__)
CORS(app)

@app.route("/crack", methods=['POST'])
def crackData():
    
    # check if lock file exists
    if subprocess.call('test -f /lock', shell=True) == 0:
        return {"lock":"lock"}
   
        


    data = request.get_json()
    dump = data['dump']
    
    # create testfile and save dump to it
    with open('/root/dump.ntds', 'w') as f:
        for line in dump:
            f.write(line+ " \n")



    # create lock file
    with open('/lock', 'w') as f:
        f.write('locked')

    
    hashcatPathFull = "/root"
    onlyHashPath= "/root/dump.ntds"
    wordlistPath = "/root/app/pwlist.txt"
    rulefilePath = "/root/app/OneRuleToRuleThemAll.rule"
    #hashcat -m 1000 ../syncer/addump.ntds ./pwlist.txt -o ./badUser.txt --status --status-timer 10  --machine-readable  --username --show -r OneRuleToRuleThemAll.rule
    str = 'hashcat -m 1000  --status --status-timer 1 --machine-readable --username --potfile-path myownteapot.potfile -r "'+ rulefilePath + '" "' + onlyHashPath + '" "' + wordlistPath + '"  | tee output.txt'
    
    thread = Thread(target=crackHashes, args=(hashcatPathFull,str,onlyHashPath))
    thread.start()

    return {"state":"Startet"}


def crackHashes(hashcatPathFull,str,onlyHashPath):
    subprocess.run(str,cwd=hashcatPathFull,shell=True)
    str = "hashcat -m 1000 --username --potfile-path myownteapot.potfile --show -o /root/badUser.txt --outfile-format 2 " + onlyHashPath
    subprocess.run(str,cwd=hashcatPathFull,shell=True)
    subprocess.call('rm /lock', shell=True)
    

@app.route("/result", methods=['GET'])
def getResult():
    # read file badUser.txt
    with open('/root/badUser.txt', 'r',encoding="utf-8") as f:
        badUser = f.read()
    badUser = badUser.split('\n')
    newBadUser = []
    for user in badUser:
        try:
            split = user.split(':')
            new = {"username":split[0],"password":split[1]}
            newBadUser.append(new)
        except:
            pass
    # remove badUser.txt
    subprocess.call('rm /root/badUser.txt', shell=True)
    # return badUser
    return {"user":newBadUser}
 

@app.route("/update", methods=['GET'])
def getUpdate():
    # read file output.txt
    with open('/root/output.txt', 'r',encoding="utf-8") as f:
        output = f.read()
        #STATUS.*UTIL

                    #STATUS  3       SPEED   312435750       1000    EXEC_RUNTIME    9.071496        CURKU   49152   PROGRESS     3068411904      51994896010     RECHASH 2       7       RECSALT 0       1       TEMP    50  REJECTED 0       UTIL    99
    stringRegex = 'STATUS.*SPEED.*EXEC_RUNTIME.*CURKU.*PROGRESS.*RECHASH .*RECSALT .*TEMP.*REJECTED.*UTIL'
    stringRegex= "STATUS.+?UTIL.*"
    

    match = re.findall(stringRegex,output)
    if not match:
        return "0"
    
    # get last element of match
    match = match[-1]
    statusRegex = 'STATUS\s+(\d+)\s+'
    progressRegex = 'PROGRESS\s+(\d+)\s+(\d+)'
    status_match = str(re.findall(statusRegex,match)[0])
    progress_match = re.findall(progressRegex,match)[0]
    temp_match = str(re.findall('TEMP\s+(\d+)',match)[0])
    speed_match = re.findall('SPEED\s+(\d+)\s+(\d+)',match)[0]

    data = {
        'status': status_match,
        'progress': progress_match[0],
        'total': progress_match[1],
        'temp': temp_match,
        'speed': speed_match[0],

    }
    return data
        
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
