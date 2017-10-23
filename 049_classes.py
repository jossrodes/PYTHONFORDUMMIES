class SayMyName:
	def __init__(self, myname):
		self.myname = myname
	def say(self):
		print "Hello, my name is", self.myname
name1 = SayMyName("Aahz")
name1.say()
