from flask import Flask
from flask import request



app = Flask(__name__)

@app.route("/crack", methods=['POST'])
def crackData():
    data = request.get_json()
    dump = data['dump']
    print(dump)
    # create testfile and save dump to it
    with open('/root/dump.ntds', 'w') as f:
        f.write(dump)
    # run ntdsxtract
    import subprocess
    hashcatPathFull = "/root"
    onlyHashPath= "/root/dump.ntds"
    wordlistPath = "/root/app/rockyou.txt"
    str = 'hashcat -m 1000 "' + onlyHashPath + '" "' + wordlistPath + '" -o ./badUser.txt '
    print(str)
    subprocess.run(str,cwd=hashcatPathFull,shell=True)
    
    return "done"

   



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)