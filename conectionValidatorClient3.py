#!/usr/bin/python

#before executing this code it MUST exist: 
#1. sshpass MUST be installed on terminal ***sudo apt-get install sshpass*** 
#2. verify position  XX (after 'validation == XX') is the same for you.

import time
import commands
import os
from daemon import runner

###########Daemonization part starts######################
class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
    def run(self):
###########Daemonization part ends########################
        while True:
            userServer = "lll"
            serverIP = "192.168.0.149"
            port = "22"
            psw = "root"
            status = commands.getstatusoutput("sshpass -p '' ssh "+userServer+"@"+serverIP+" -p "+port)
            if status[0] == 0: # return 0 whit no errors
                print("Key found")
            elif status[0] == 1280: #Error Server found but password does not match
                print("Key not found... Trying to copy public key")
                key=commands.getoutput("./untitled.sh")
                print(key)
            else: #any other error
                print("Server not found")
            time.sleep(5)
###########Daemonization part starts######################
app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
###########Daemonization part ends########################