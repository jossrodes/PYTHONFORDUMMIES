try:
	x = int(x)
except TypeError:
	raise TypeError("%r is not a valid integer" % x)