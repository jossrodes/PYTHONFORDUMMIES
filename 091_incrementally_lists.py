L1 = ['spam', 'spam', 'spam', 'baked beans', None, 'spam', 'spam']
L2 = []
for i in L1:
	if i is not None:
		L2.append(i)
a = [8, 3, 5, 11]
b = ('eggs', 'spam')
c = zip(a, b)
print c
zip(*c)
a = [8, 3, 5, 11]
for I, item in enumerate(a):
print (I, item),