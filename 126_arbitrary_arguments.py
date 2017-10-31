def a_function(a, b, *args, **kwargs):
	print "a is", a
	print "b is", b
	print "*args is this tuple:", args
	print "**kwargs is this dictionary:", kwargs
a_function(1, '2', 'three', 'blind', 'mice', see="how", they="run")