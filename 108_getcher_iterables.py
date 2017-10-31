for element in range(1,4): # range
	print element
for element in [1, 2, 3]: # list
	print element
for key in {'one':1, 'two':2}: # dictionary
	print key
for line in open("myfile.txt"): # text file
	print line
for value in mydict.itervalues(): # iterator object
	print value
for key, value in mydict.iteritems(): # tuple unpacking
	print key, value