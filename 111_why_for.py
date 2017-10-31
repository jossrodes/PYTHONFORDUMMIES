for i in range(5):
	if i < 3:
		i = "more spam!"
	else:
		i = "bleargh!"
print i
for i in range(5):
	print i,
	if i < 3:
		i = "more spam!"
	else:
		i = "bleargh!"