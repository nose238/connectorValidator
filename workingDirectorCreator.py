import commands

#Verify if ssh connection exists (public_keys).
def connectionValidator():
	txtConnection = open("sshStatus.txt", "r")
	status = txtConnection.read()
	#if status == 0, connection exists
	return int(status)

if connectionValidator() != 0:
	print("You have no SSH connection")
else:
	##########read server data
	temp = 0 #used to eliminate the last character in strings
	txt = open("userServer.txt", "r")
	userServer = txt.read()
	temp = len(userServer)
	userServer = userServer[:temp-1]
	txt.close()
	txt = open("serverIP.txt", "r")
	serverIP = txt.read()
	temp = len(serverIP)
	serverIP = serverIP[:temp-1]
	txt.close()
	txt = open("portServer.txt", "r")
	portServer = txt.read()
	temp = len(portServer)
	portServer = portServer[:temp-1]
	txt.close()
	##########read client data
	txt = open("SOPORTE/clientName.txt", "r")
	clientName = txt.read()
	txt.close() 
	txt = open("SOPORTE/hostName.txt", "r")
	hostName = txt.read()
	txt.close() 
	txt = open("SOPORTE/ipHost.txt", "r")
	ipHost = txt.read()
	txt.close() 
	########## 
	groupWorkingDirectory = commands.getoutput("sshpass -p '' ssh -o StrictHostKeyChecking=no "
		+userServer+"@"+serverIP+" -p "+portServer+
		" ' if [ -d /"+clientName+"/ ]; then echo \"exists\" ; else mkdir "+clientName+"; fi ' ")
	
	clientWorkingDirectory = commands.getoutput("sshpass -p '' ssh -o StrictHostKeyChecking=no "
		+userServer+"@"+serverIP+" -p "+portServer+
		" ' if [ -d /"+hostName+ipHost+"/ ]; then echo \"exists\" ; else cd "+clientName+"; mkdir "+hostName+"@"+ipHost+"; fi ' ")

