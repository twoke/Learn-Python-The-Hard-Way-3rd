# this one is like your scripts with argv

def print_two(*args):
	arg1, arg2 = args
	print "arg1:%r, arg2:%r" % (arg1, arg2)
# ok
def print_two_again(arg1, arg2):
	print "arg1:%r, agr2:%r" % (arg1, arg2)

# this just take one orgument
def print_one(arg1):
	print "arg1:%r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("zed", "Shaw")
print_two_again("zed", "shaw")
print_one("first!")
print_none()
