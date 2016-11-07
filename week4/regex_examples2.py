# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# Basically these are the rules: I, X, C and M can be repeated up three times
# to represent one number. I, II and III - legit. IIII - NOT. Same with the others.
# I = 1, II = 2, III = 3, VI = 6, so they are additive. But, as we know, they can be the
# opposite. Like IV = 4 (literally 5 - 1).
# The fives characters can not be repeated. VV - NOT 10, not legit. X - 10.
# Same with LL and DD.
# We read Roman numerals left to right. This matters a lot! DC = 600,
# while CD = 400. CI = 101 and IC is not even valid.

# Now we want to write a pattern that checks whether a given number is 
# valid or not.

import re

# Roman numerals are always written highest to lowest. So we should start with
# the Ms - thousands.

pattern = r'^M?M?M?$'

# We don't want anything before the number so we put '^' at the beggining of
# the string. It means 'the beggining of the string' ;d It is the opposite of '$'

# '?' means that the character before it is optional. We don't always want two
# or three Ms, or even one. So we shouldn't set a rule that we must have it.

result = re.search(pattern, 'M')
print(result.string)

result = re.search(pattern, 'MM')
print(result.string)

result = re.search(pattern, 'MMM')
print(result.string)

result = re.search(pattern, 'MMMM')
# print(result.string) - this will crash. MMMM does not match our pattern, so
# re.search() will return None.

# Then we should check for hundreds:

# 100 = C
# 200 = CC
# 300 = CCC
# 400 = CD
# 500 = D
# 600 = DC
# 700 = DCC
# 800 = DCCC
# 900 = CM

pattern = r'^M?M?M?(CM|CD|D?C?C?C?)$'

# What????
# So here are the possibilities for hundreds:
# 
# C, CC, CCC - 100, 200, 300, matches C?C?C?
# One D can be combined with these combination of Cs:
# DC, DCC, DCCC - 600, 700, 800, matches D?C?C?C?
#
# So the pattern "D?C?C?C?" matches C, CC, CCC, D, DC, DCC, DCCC -
# 100, 200, 300, 600, 700, 800
# But there are other hundreds so we could have one of the numbers above OR
# 400. 400 = CD. Remember the word OR. This is where the '|' symbole comes in handy.
# We match CD OR D?C?C?C?.
# Aaaand same thing happens with CM - 900. So now we have (CM|CD|D?C?C?C?) to
# match the hundreds. The parentheses are necessary for the OR.

# And now the tens:
# 10 20 30 40 50 60 70 80 90 100
# X XX XXX XL L LX LXX LXXX XC
pattern = r'^M?M?M?(CM|CD|D?C?C?C?)(L?X?X?X?|LX|XC)$'

# And ones:
# 1 2 3 4 5 6 7 8 9
# I II III IV V VI VII VIII IX
pattern = r'^M?M?M?(CM|CD|D?C?C?C?)(L?X?X?X?|LX|XC)(V?I?I?I?|IV|IX)$'

# Simplify!

pattern = r'^M{0,3}(CM|CD|D?C{0,3})(L?X{0,3}|LX|XC)(V?I{0,3}|IV|IX)$'

# M{0,3} simply means that you can have from 0 to 3 Ms. Same with others.