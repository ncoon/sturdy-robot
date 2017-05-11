def meanarterial():
	# Mean Arterial Pressure Calculator!
	promptsystolic = raw_input ('Enter systolic blood pressure. ')
	print '\n'
	promptdiastolic = raw_input ('Enter diastolic blood pressure. ')
	print '\n'
	pulsepressure = int(promptsystolic) - int(promptdiastolic)
	MeanArterialPressure = int(promptdiastolic) + (int(pulsepressure) / 3)
	print 'Mean Arterial Pressure is ' + str(int(MeanArterialPressure)) + '.'
	print '\n'
	return
