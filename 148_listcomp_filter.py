filtered_list = [x for x in range(50) if x % 5 == 0]
filtered_list

filtered_list = []
for x in range(50):
	if x % 5 == 0:
		filtered_list.append(x)