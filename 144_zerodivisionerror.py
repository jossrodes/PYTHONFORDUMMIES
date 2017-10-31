try:
	x = 1/0
except ZeroDivisionError, detail:
	print "Oops,", detail
Oops, integer division or modulo by zero