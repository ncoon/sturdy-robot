def meanarterial():
	# Mean Arterial Pressure Calculator!
	promptsystolic = eval(input ('Enter systolic blood pressure. '))
	print('\n')
	promptdiastolic = eval(input ('Enter diastolic blood pressure. '))
	print('\n')
	pulsepressure = int(promptsystolic) - int(promptdiastolic)
	try:
		MeanArterialPressure = int(promptdiastolic) + (int(pulsepressure) / 3)
		print(('Mean Arterial Pressure is ' + str(int(MeanArterialPressure)) + '.'))
	except:
		print('Please enter valid integers when prompted.\n')
	print('\n')
	return
