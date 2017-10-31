def f(mylist, data):
	newlist = mylist[:] # make a copy of mylist
	for i in range(len(mylist)):
		newlist[i] = mylist[i] + data
	return newlist
alist = [1, 2, 3]
x = f(alist, 5)
print x
print alist