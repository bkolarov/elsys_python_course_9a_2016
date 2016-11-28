# Okay, functions are objects, we can pass them and store them. But did you know
# we can define new ones in another function?

def give_me_food(command=None):
	
	# we define a function within our function
	def make_me_a_sandwich():
		# we have access to the value of the variable command
		if command == 'sudo':
			print ('Here you go, a giant pepperoni sandwich!')
		else:
			print("Why don't you make it yourself?")

	make_me_a_sandwich()

give_me_food()
give_me_food('sudo')


print()
print()

# Actually I must say it more specific. Yes, we have access to the parameters
# but it is read only. This means that if we try to write new value to the
# parameter, we will have a KABOOM!

def give_me_food(command, food_string):

	def make_me_a_sandwich():

		if command == 'sudo':
			
			print (food_string)
		else:
			# no. you cannot do that. not like this.
			food_string = "Why don't you make it yourself?"
			print(food_string)

	make_me_a_sandwich()
	print ('food_string: ' + food_string)

give_me_food(None, 'Macarroni')
give_me_food('sudo', 'Pasta')