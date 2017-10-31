try:
	x = raw_input("Enter an integer: ")
	y = int(x)
	print "Your number was", y
except (TypeError, ValueError):
	print "That didn't