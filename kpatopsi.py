def kpatopsi():
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
def goback():
	promptgoback = raw_input ('Go back to calculator? 1 = Yes | 0 = No ')
	print '\n'

	if float(promptgoback) == 1:
		kpatopsi()
	elif float(promptgoback) == 0:
		return
	else :
		return
