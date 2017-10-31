class Employee:
	def __init__(self, lastname, firstname=None):
		self.lastname = lastname
		self.firstname = firstname
	def __str__(self):
		if self.firstname:
			return "%s %s" % (self.firstname, self.lastname)
		else:
			return self.lastname
			
a = Employee('Aahz')
b = Employee('Maruch', 'Stef')
c = 'Maruch, Stef'
print a
print b
print c
