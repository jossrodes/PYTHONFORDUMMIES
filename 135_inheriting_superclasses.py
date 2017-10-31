class A:
	def foo(self):
	print "foo called in A"
class B:
	def foo(self):
		print "foo called in B"
	def bar(self):
		print "bar called in B"
class C(A,B):
	pass
	
x = C() # Create an instance of C
x.foo() # Call the foo() method
x.bar() # Call the bar() method
