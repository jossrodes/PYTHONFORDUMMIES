mystring = "European swallow"
myregex = re.compile("European")
myregex.sub("African", mystring) # method
re.sub('European', 'African', mystring) # function