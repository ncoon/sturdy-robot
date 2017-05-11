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
	print '\n'
	time = ((int(promptpsi) - 200) * float(promptconstant)) / int(promptlpm)
	print time
	print '\n'
	return
