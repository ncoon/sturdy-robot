def parkland():
	# Parkland Formula Calculation!
	# V = 4*m*(A*100)
	promptkg = eval(input ('Enter patient weight in kg. '))
	print('\n')
	promptburn = eval(input ('Enter burn percentage. (Only second-degree or greater) '))
	print('\n')
	calculation = 4 * int(promptkg) * int(promptburn)
	first_plan = 'over the first 8 hours in the 24 hour period. '
	second_plan = 'over the last 16 hours in the 24 hour period. '
	halffluid = int(calculation) / 2
	print(('Administer ' + str(int(halffluid)) + 'ml ' + first_plan + 'Administer ' + str(int(halffluid)) + 'ml ' + second_plan))
	print('\n')	
	return
