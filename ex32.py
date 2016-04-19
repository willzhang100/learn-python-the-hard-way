the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#first for loop goes through a list
for number in the_count:
	print "This is count %d" % number

#same
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#mixed list use %r
for i in change:
	print "I got %r" % i

#built lists, start with empty
elements = []

"""
for i in range(0,6):
	print "Adding %d to the list." % i
	#append
	elements.append(i)
"""
elements = range(0,6)

#print
for i in elements:
	print "Element was: %d." % i