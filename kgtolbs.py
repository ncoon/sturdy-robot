def kgtolbs():
	# Kg to lbs & lbs to kg converter
	promptask = raw_input ('Convert kg>lbs (1) or lbs>kg? (2) ')
	print '\n'
	if int(promptask) == 1:
		promptkg = raw_input('Enter weight of patient in kilograms(kg). ')
		kgtolbs = float(promptkg) * 2.204622
		print str(float(kgtolbs)) + ' lbs. '
	elif int(promptask) == 2:
		promptlbs = raw_input('Enter weight of patient in pounds(lbs). ')
		lbstokg = float(promptlbs) * 0.453592
		print str(float(lbstokg)) + ' kg. '
	print '\n'
	promptgoagain = raw_input ('Back to converter (1) or main menu?(2) ')
	print '\n'
	if int(promptgoagain) == 1:
		Kgtolbs()
	elif int(promptgoagain) == 2:
		return
	else : return
