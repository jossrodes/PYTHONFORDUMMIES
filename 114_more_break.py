mystring = "larch"
vowels = set('aeiou')
for a in mystring:
	if a in vowels:
		print mystring, "has a vowel"
		break
	else:
		print mystring, "does not have a vowel"