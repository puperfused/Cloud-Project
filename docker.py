#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

osname = cgi.FormContent()['os_name'][0]
cont_no =  cgi.FormContent()['container_no'][0]

#print osname + " "+cont_no
i=0
commands.getstatusoutput("sudo systemctl restart docker")
cont_ip_list = {}
while i<int(cont_no):
	commands.getoutput("sudo docker run -dit --privileged=true --name container{0} {1}".format(i,osname))
	ipAddr = commands.getstatusoutput( "sudo docker inspect container{} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(i))
	cont_ip_list['container{}'.format(i)] = ipAddr[1].strip('"')
	i+=1
	

print "Service Started at Following IP's:"
print "<br/>"
i=0;
while i<int(cont_no):
	print "Container {} Running at IP: ".format(i) + cont_ip_list['container{}'.format(i)]
	print "<br/>"
	#print "working..."
	i+=1
#print "done..."
"""
if run_status[0]==0:
	print "ran successfully... "
else:
	print "failed to open ..."
"""
