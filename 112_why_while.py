def process(a):
	print a,
	
mylist = [1, 2, None, 4, 5]
data = mylist.pop()
while data:
	process(data)
	data = mylist.pop()