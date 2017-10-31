myquote = open('quotes.txt')
myquote.read(27)
myquote.readlines()
for line in myquote:
	print line.rstrip()