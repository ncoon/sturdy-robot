def kPatoPSI():
	promptkpaorpsi = raw_input ('Convert kPa>PSI = 1 or PSI>kPa = 2? ')
	print '\n'
	if int(promptkpaorpsi) == 2:
		print '\n'
		promptpsi = raw_input ('Enter PSI. ')
		psitokpa = (float(promptpsi) / 0.145038)
		print str(float(psitokpa)) + ' kPa. '
	elif int(promptkpaorpsi) == 1:
		print '\n'
		promptkpa = raw_input ('Enter kPa. ')
		kpatopsi = (float(promptkpa) * 0.145038)
		print str(float(kpatopsi)) + ' PSI. '	
		print '\n'
	promptgoback = raw_input ('Go back to calculator? 1 = Yes | 0 = No ')
	print '\n'
	if str(promptgoback) or str(promptgoback) == '':
		return
	if int(promptgoback) < 0 or int(promptgoback) >= 2:
		return
	elif int(promptgoback) == 1:
		kPatoPSI()
	elif int(promptgoback) == 0:
		return
kPatoPSI()
