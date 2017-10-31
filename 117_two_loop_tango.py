mylist1 = ['rock', 'paper', 'scissors']
mylist2 = ['scissors', 'rock', 'paper']
mylist3 = ['paper', 'scissors', 'rock']
for a, b, c in zip(mylist1, mylist2, mylist3):
	print "%s beats %s but not %s" % (a,b,c)