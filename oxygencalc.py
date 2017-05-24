def oxygencalc():
	# Oxygen Tank Calculation!
	# ((PSI - 200) * Tank Constant) / Flow Rate (Litres per minute)
	D = 0.16   ## 350liters of O2
	E = 0.28   ## 625liters of O2
	M = 1.56   ## 3000liters of O2
	Safe = 200
	promptpsi = raw_input ('Enter tank PSI. ')
	print '\n'
	promptlpm = raw_input ('Flow rate in Liters per minute. ')
	print '\n'
	promptconstant = raw_input ('Tank size? D=0.16/E=0.28/M=1.56 ')
	try:
		if str(promptconstant) == 'D':
			constant = D
		elif str(promptconstant) == 'E':
			constant = E
		elif str(promptconstant) == 'M':
			constant = M
		elif str(promptconstant) == 'd':
			constant = D
		elif str(promptconstant) == 'e':
			constant = E
		elif str(promptconstant) == 'm':
			constant = M
		else:
			constant = float(promptconstant)
	except:
		print 'Please enter either the number or corresponding letter. ' 
	print '\n'
	time = ((int(promptpsi) - 200) * float(constant)) / int(promptlpm)
	print time
	print '\n'
	return
