# So, as you know, in python everything is? I know! A cow!
# Okay, close enough.. Everything in python is an object. Every variable and every
# function. This is the core of this lesson - each function is also an object.

# this is a function

def make_me_a_sandwich():
	print("Why don't you make it yourself?")

# and since make_me_a_sandwich is an object we can pass it, store it etc.

def tell_mum_to_make_you_a_sandwich(make_me_a_sandwich):
	return make_me_a_sandwich()

tell_mum_to_make_you_a_sandwich(make_me_a_sandwich)