user_input = raw_input("Enter an integer: ")
try:
	number = int(user_input)
	print "You entered", number
except ValueError:
	print "Integers, please!"