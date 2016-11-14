# So except programming languages, there are of course human languages. Like English!
# Aaaaand in English some words are called nouns, right? 
# Aaaaand these nouns can be plurals right?
# So that is what we are going to talk about here. Or to be more specific
# we are going to talk about how to turn nouns into plural nouns.

# To see the rules for turning nouns into plural nouns checkout this link:
# http://www.diveintopython3.net/generators.html#divingin

# So let's begin, We want to apply some rules to a string, and if the string
# matches one of those rules this means we can turn it intu a plural noun.

# REGEX!!!

import re

# Yes, we are using functions now.
'''
def plural(noun):
	if (re.search(r'[sxz]$', noun)): # noun = 'class' or 'tax' or 'waltz'

		# basically we are replacing the end of the string wirh 'es'.
		# This is equal to noun + 'es'
		return re.sub(r'$', 'es', noun) 

	# '^' in square brackets this means match any single character that is 
	# not in the brackets.
	elif re.search(r'[^aeioudgkprt]h$', noun): # noun = 'coach' or 'couch'

		return re.sub(r'$', es, noun)

	elif re.search(r'[^aeiou]y$', noun): # noun = 'try'

		return re.sub(r'y$', 'ies', noun)

	else: # noun = 'day', 'toy', 'cheetah'

		return noun + 's' 

'''

# break it into functions

def match_sxz(noun):

	return re.search(r'[sxz]$', noun)


def apply_sxz(noun):

	return re.sub(r'$', 'es', noun)


def match_h(noun):

	return re.search(r'[^aeioudgkprt]h$', noun)


def apply_h(noun):

	return re.sub(r'$', es, noun)


def match_y(noun):

	return re.search(r'[^aeiou]y$', noun)


def apply_y(noun):

	return re.sub(r'y$', 'ies', noun)


def match_default(noun):

	return True

def apply_default(noun):

	return noun + 's'

# Tuples? Remember them?
# Also do you remember that everything in python is an object?
# Well we can have a tuple of functions, because functions are objects.

rules = (
	(match_sxz, apply_sxz),
	(match_h, apply_h),
	(match_y, apply_y),
	(match_default, apply_default)
)

def plural(noun):
	for matches_rule, apply_rule in rules:
		if matches_rule(noun):
			return apply_rule(noun)

# So lets simplify even more!
# We have a lot of functions that do pretty much the same. 
# Half of the functions check if a given string matches a rule. The other
# half applies the rule.

def build_match_and_apply_functions(rule_pattern, search_pattern, replace):
	def match_rule(word):
		return re.search(rule_pattern, word)

	def apply_rule(word):
		return re.sub(search_pattern, replace, word)

	return (match_rule, apply_rule)

patterns = \
  (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')                                 
  )

rules = [build_match_and_apply_functions(rule_pattern, search_pattern, replace)
			for rule_pattern, search_pattern, replace in patterns]

print (plural('try'))