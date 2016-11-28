def give_me_food(command, food_string):

	def make_me_a_sandwich():

		# this little piece of magic can help
		nonlocal food_string

		if command == 'sudo':
			print (food_string)
		else:
			
			food_string = "Why don't you make it yourself?"
			print(food_string)

	make_me_a_sandwich()
	print ('food_string: ' + food_string)

give_me_food(None, 'Macarroni')
give_me_food('sudo', 'Pasta')