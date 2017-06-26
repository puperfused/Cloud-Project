#!/usr/bin/python2

import commands
import re
import cgi 

print "content-type: text/html"
#print

userName=cgi.FormContent()['username'][0]
passWord=cgi.FormContent()['password'][0]

#print userName
#print "<br/>"
#print passWord

var=commands.getstatusoutput("cat /detail/user.txt | grep {}".format(userName))
if var[0]!=0:
	print "not valid user"
else:
	s=var[1].split(":")
	if s[1]==passWord:
		#print "valid user"
		print "location: ../menu.html"
		print
	else:
		#print "incorrect pasword"
		print "location: ../login.html"
		print
#print "hi"
