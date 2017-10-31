x = 'x'
y = 'x**2'
z = 'x**x'
print x, y.rjust(4), z.rjust(6)
print "=" * 14
for n in range(1,6):
	nn = str(n**2)
	nnn = str(n**n)
	print n, nn.rjust(4), nnn.rjust(6)