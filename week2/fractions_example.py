from fractions import Fraction

# That's right. You can have fractions in Python.

# want the fraction 1 / 3? Here you go:

fraction_1 = Fraction(1, 3)
print ("Fraction(1, 3) = " + str(fraction_1))

# 2/4 = 1/2 right?

fraction_2 = Fraction(2,4)
print ("Fraction(2, 4) = " + str(fraction_2))

# yes.

fraction_sum = fraction_1 + fraction_2
print ("Fraction(1, 3) + Fraction(2, 4) = " + str(fraction_sum))