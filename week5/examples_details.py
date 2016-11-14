# square brackets? What the shmock are these?
# Simply [] means 'match one of the characters inside'.
# [abc] is equal to (a|b|c). But here is the difference between the two approaches:
# You can have (ab|cd|ef), but you can't do the same with square brackets.

import re

# So this has a result

print (re.search(r'[abc]', 'Day'))


# This one hasn't

print (re.search(r'[abc]', 'Toy'))

print()

# Example for replacing:

print (re.sub(r'[abc]', 'o', 'Park'))

# And another one:

print (re.sub(r'[abc]', 'o', 'caps'))

# re.sub() will replace all matches in the string, not only the first one!

print()

# '^'?? This seems familiar. Oh yeah.. This means the beggining of the string.
# WRONG!!! In square brackets this means match any single character that is 
# not in the brackets. [^abc] - 'o' matches, 'k' - matches, 'a' - nope.

# Lets try it:

print (re.search(r'[^abc]$', 'KARTOF').string)

print (re.search(r'[^abc]$', 'automatic'))

print()

# And in our case: 
print (re.search(r'[^aeioudgkprt]h$', 'path'))

print (re.search(r'[^aeioudgkprt]h$', 'peach').string)