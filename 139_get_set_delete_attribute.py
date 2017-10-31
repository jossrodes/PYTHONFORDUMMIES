class MyClass(object):
	def __init__(self):
		self._x = 0
	def getx(self):
		print "Getting _x"
		return self._x
	def setx(self, x):
		if x < 0:
			raise ValueError("Negative values prohibited: %r" %
			x)
		self._x = x
		print "Setting _x"