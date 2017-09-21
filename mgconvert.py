def mgconvert():
	# Milligram / Microgram Converter
	promptask = raw_input ('Convert mg>ug(mcg) (1) or ug(mcg)>mg? (2) ')
	print '\n'
	if int(promptask) == 1:
		promptmg = raw_input('Enter weight mg. ')
		mgtoug = float(promptmg) * 1000
		print str(float(mgtoug)) + ' ug(mcg). '
	elif int(promptask) == 2:
		promptug = raw_input('Enter weight ug(mcg). ')
		ugtomg = float(promptug) / 1000
		print str(float(ugtomg)) + ' mg. '
	print '\n'
def goback():
	promptgoagain = raw_input ('Back to converter (1) or main menu?(2) ')
	print '\n'
	if int(promptgoagain) == 1:
		mgconvert()
	elif int(promptgoagain) == 2:
		return
	else:
		return
