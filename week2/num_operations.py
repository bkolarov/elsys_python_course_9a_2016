#float division

float_division = 11 / 2

print ("11 / 2 = %.2f" % float_division)
print (float_division)
print (type(float_division))

print ()

# something like integer division

int_division = 11 // 2

print ("11 // 2 = %d" % int_division)
print (type(int_division))

print ()

# !! be careful here. When integer-dividing negative numbers, the // operator rounds "up" to the nearest integer.
# mathematically speaking it rounds "down" because of the '- sign

negative_int_division = -5 // 2

print ("-5 // 2 = %d" % negative_int_division)

negative_int_division = 5 // -2

print ("5 // -2 = %d - same thing" % negative_int_division)

# BUT!

negative_int_division = -5 // -2
print ("BUT!!!")
print ("-5 // -2 = %d" % negative_int_division)

print (type(negative_int_division))

# Be careful with the // opeartor

# if the division has a float number, then the result will be of type float, but with zeroes after the floating point

print()

float_int_division = 11.0 // 2
print ("11.0 // 2 = %.2f" % float_int_division)

float_int_division = 11 // 2.0
print ("11 // 2.0 = %.2f - same thing" % float_int_division)

float_int_division = 11.0 // 2.0
print ("11.0 // 2.0 = guess what.. yep - %.2f" % float_int_division)

float_int_division = -11.0 // 2.0
print ("-11.0 // 2.0 = %.2f - rules for the minus sign are the same,\n\t\t\tjust the result is float" % float_int_division)

print(type(float_int_division))

print ()

# 2 ** 4 - 2 is raised to the power of 4

powered = 4 ** 2
print ("4 ** 2 = %d" % powered)
print(type(powered))

powered = 4.0 ** 2
print ("4.0 ** 2 = %.2f" % powered)
print(type(powered))

print ()

# % - the remainder after performing integer division

remainder = 11 % 2
print ("11 %% 2 = %d" % remainder)
print ("11 / 2 = 5; 5 * 2 = 10; remainder = 1")