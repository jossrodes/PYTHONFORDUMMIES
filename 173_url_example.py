import urllib2
page = urllib2.urlopen('http://www.python.org/doc/current/modindex.html')
page
for line in page:
	sys.stdout.write(line)
page=urllib2.urlopen('http://www.python.org/idontexist.html')
print page.info()
redirect = urllib2.urlopen('http://www.livejournal.com/users/firecat')
redirect.geturl()
