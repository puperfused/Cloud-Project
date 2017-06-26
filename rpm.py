#!/usr/bin/python2

import cgi
import commands
print "Content-Type: text/html"
print

#print "hello"
#ipAddress = cgi.FormContent()['ip'][0]
packageName = cgi.FormContent()['rpm'][0]

#print "hello"

status = commands.getstatusoutput("sudo yum install {} -y".format(packageName))

if status[0]==0:
	print "software installed successfully .."
else:
	print "you are fucked up .."
