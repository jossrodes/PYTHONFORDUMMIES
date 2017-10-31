mystring = 'Your father smelt of elderberries!'
print re.findall('[aeiou]', mystring)

mystring = 'Your father smelt of elderberries!'
vowels = re.compile('[aeiou]')
vowels.findall(mystring)