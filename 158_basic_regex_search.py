zipcode = r'Zip:\s*\d\d\d\d\d'
ddr = "Street address: 342 Anywhere Rd \n Zip: 32433"
re.search(zipcode, addr)
mystring = "foo"
print re.search(zipcode, mystring)