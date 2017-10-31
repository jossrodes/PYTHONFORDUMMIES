result = []
cache = {}
for key in mylist:
	if key in cache:
		result.append(cache[key])
	else:
		value = getValue(key)
		cache[key] = value
		result.append(value)
result = []
cache = {}
for key in mylist:
	if key in cache:
		result.append(cache[key])
	else:
		# Add to cache and append to result
		result.append(cache.setdefault(key, getValue(key)))
result = []
cache = {}
	for key in mylist:
		try:
			result.append(cache[key])
		except KeyError:
			# Add to cache and append to result
			result.append(cache.setdefault(key, getValue(key)))
L = [(1, 'pear tree'), (5, 'golden rings'), (1, 'partridge')]
d = {}
for key,value in L:
	d.setdefault(key, []).append(value)
d