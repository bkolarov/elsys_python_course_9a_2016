# So someone saw an animal and decided it is a cow. Well it is actually
# a bull. So that guy needs to search and replace cow with bull. Easy!
string = 'There is a cow!!!'

print (string)

string = string.replace('cow', 'bull')

print (string)

print ()

# But where is that cow? In Moscow of course!
string = 'When I was in Moscow I saw a cow'

string = string.replace('cow', 'bull')

print (string)

print()

# Mosbull? I heard there are mostly bullies there. Get it? Get it?
# Agh.. never mind. 
# So u see the problem here is that wherever the word 'cow' occurs 
# it will be replaced with 'bull'.

# Solution? No problem, I can just do this:

string = 'When I was in Moscow I saw a cow'

string = string[:-3] + string[-3:].replace('cow', 'bull')

print (string)

# If you can't tell me why this solution is like worst of the worst
# please find out as soon as you can.

string = 'When I was in Moscow I saw a cow!!'

string = string[:-3] + string[-3:].replace('cow', 'bull')

print (string)

# See the problem? The word 'cow' has a different position in the string.'

print ()

# Time to show you how it's done like a boss. We will use regular expressions (regex).

import re

string = 'When I was in Moscow I saw a cow'

expression = r'cow$'
string = re.sub(expression, 'bull', string)

print (string)

# So we have a regex pattern 'cow$' and it works like a charm.
# Well almost..

# Lets get back to this example

string = 'When I was in Moscow I saw a cow!!!'

string = re.sub(expression, 'bull', string)

print (string)

# Does it work? No. the '$' sign means the end of the string.
# But here after cow there are more other symbols, not the end of the string.

print ()

string = 'When I was in Moscow I saw a cow!!!'

expression = r'cow\b'
string = re.sub(r'cow\b', 'bull', string)

print (string)

# Again something about Mosbull.. I'm sick of that place! 


string = 'When I was in Moscow I saw a cow!!!'

expression = r'\bcow\b'
string = re.sub(expression, 'bull', string)

print (string)

# Finally! The '\b' means there must be a word boundary right here.
# So this expression will work in this and similar cases too:

string = 'When I was in Moscow I saw a,cow!!!'

string = re.sub(expression, 'bull', string)

print (string)

string = 'When I was in Moscow I saw a...!cow!!!'

string = re.sub(expression, 'bull', string)

print (string)

# You get the idea