def safe_read(filename):
	f = open(filename)
	try:
		data = f.read()
	except IOError:
		data = None
	finally:
		f.close()
	return data