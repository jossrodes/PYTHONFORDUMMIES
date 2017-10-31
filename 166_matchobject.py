my_regex = re.compile('py+thon')
mystring = "pyyython is a suuuper programming language"
mymatch = my_regex.match(mystring)
mymatch

mymatch.group(0)
y.groups()
y.groupdict()
mymatch.span(0)

if mymatch:
	print 'Match found'
else:
	print 'No match'