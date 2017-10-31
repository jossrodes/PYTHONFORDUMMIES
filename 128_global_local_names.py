# groucho.py
a_book = "man's best friend"
print "outside of a dog, a book is", a_book
def a_dog():
	a_book = "too dark to read"
	print "inside of a dog, it's", a_book
a_dog()
	print "we're back outside of the dog again"
	print "and a book is again", a_book