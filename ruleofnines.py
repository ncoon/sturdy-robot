# Rule of Nines
def ruleofnines():
	promptpt = eval(input ('Adult = 1 | Pediatric = 2 '))
	print('\n')
	if int(promptpt) == 1: ####ADULT
		promptnines = eval(input ('Anterior = 1 | Posterior = 2 '))
		print('\n')
		if int(promptnines) == 1:
			print('Head 4.5%, Trunk 18%, Arms 4.5% (Each), Legs 9% (Each), 	Genitalia/Perineum 1% ')
			print('\n ')
		elif int(promptnines) == 2:
			print('Head 4.5%, Trunk 18%, Arms 4.5% (Each), Legs 9% 	(Each) ')
			print('\n ')
		promptgoback = eval(input ('Rule of Nines = 1 | Menu = 2 '))
		if int(promptgoback) == 1:
			ruleofnines()
			print('\n ')
		elif int(promptgoback) == 2:
			return
			print('\n ')
	elif int(promptpt) == 2: ########PEDIATRIC
		print('For every year > 1 year old add 0.5% to each leg and subtract 1% from the head. Use this formula until adult values are reached. ')
		print('\n')
		promptinfant = eval(input ('Anterior = 1 | Posterior = 2 '))
		print('\n')
		if int(promptinfant) == 1:
			print('Head 9%, Trunk 18%, Arms 4.5% (Each), Legs 7% (Each), Genitalia/Perineum 1% ')
			print('\n ')
		elif int(promptinfant) == 2:
			print('Head 9%, Trunk 18%, Arms 4.5% (Each), Legs 7% (Each) ')
			print('\n ')
def goback():

	promptgoback = eval(input ('Rule of Nines = 1 | Menu = 2 '))
	if int(promptgoback) == 1:
		ruleofnines()
		print('\n ')
	elif int(promptgoback) == 2:
		return
		print('\n ')
	else:
		return
		print('\n')

