# formatting

person = 'Pesho'
description = 'awesome'

person_description = '{0} is not {1}.'.format(person, description)

print (person_description)

print ()

# probably you may have guessed that:

person_description = '{1} is not {0}.'.format(person, description)
print (person_description)

# yeah, Pesho is not awesome and awesome is not Pesho.

print ()

# and now with some imagination we can do this:

days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']

message = 'I\'d like the weekend to start on {0[0]} and end on {0[4]}'.format(days)
print (message)

print ()

# and here is a thing, called specifier

import math

some_string = 'Pi is approximately {0:.3f}'.format(math.pi)
print (some_string)

# So.. you know the {0} part. What we did there is that we added a specifier.
# By adding this :.3d we said 'show only three digits after the floating point'

print ()
print ()

# And of course tehere are some basics

multiline_string = 'this\nis\nan annoying\nmultiline\nstring.'
print (multiline_string)

list_of_lines = multiline_string.splitlines()
uppercase_list_of_lines = [line.upper() for line in list_of_lines]

# List comprehension!! OMG WOW :OOOO When you start coding in other languages like 
# C and JAVA you will understand my joy

print (uppercase_list_of_lines)

each_line_ch_count = [len(line) for line in list_of_lines]

print (each_line_ch_count)