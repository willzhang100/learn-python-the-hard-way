#like argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#without *args
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#one arg
def print_one(arg1):
	print "arg1: %r" % arg1
	
#no arg
def print_none():
	print "I got nothin'."
	
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()