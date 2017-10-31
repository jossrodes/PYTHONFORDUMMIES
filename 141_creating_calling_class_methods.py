class E(object):
	def g(cls, x):
		return cls.__name__, x
	g = classmethod(g)
print E.g(3)
print E().g(3)