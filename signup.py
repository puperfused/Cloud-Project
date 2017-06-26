#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

userName=cgi.FormContent()['newuser'][0]
passWord=cgi.FormContent()['newpass'][0]

#print userName
#print "<br/>"
#print passWord

fh=open('/detail/user.txt','a')
fh.write("{0}:{1}\n".format(userName,passWord))
#print "User Successfully added.. "
#print "hi"
