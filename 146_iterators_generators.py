n = [1, 3, 6, 4, 3, 6, 3, 234]
m = [1, 2, 3, 5, 6, 7, 8, 9]
for i in itertools.imap((lambda x, y: x*y), m, n):
	print i

n = [1, 3, 6, 4, 3, 6, 3, 234]
for i in itertools.imap((lambda x, y: x*y), n, itertools.count()):
	print i

for i in itertools.islice(xrange(62), 6, 62, 3):
	print i