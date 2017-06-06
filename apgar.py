def apgar():
	print 'APGAR test is to be done at 1 minute and 5 minutes post delivery.(Repeated at 5 minute intervals if scores are low.) '
	print ''
	print '0 = Blue or pale all over '
	print '1 = Blue at extremities, body pink '
	print '2 = No cyanosis, body and extremities pink '
	print '\n'
	promptcomplexion = raw_input ('Enter value for Complexion (Appearance). ')
	print '\n'
	print '0 = Absent '
	print '1 = <100 beats per minute '
	print '2 = >100 beats per minute '
	print '\n'
	promptpulsescore = raw_input ('Enter value for Pulse. ')
	print '\n'
	print '0 = No response to stimulation ' 
	print '1 = Grimace on suction or aggressive stimulation '
	print '2 = Cry on stimulation '
	print '\n'
	promptgrimace = raw_input ('Enter value for Grimace. ')
	print '\n'
	print '0 = None '
	print '1 = Some flexion '
	print '2 = Flexed arms and legs that resist extension '
	print '\n'
	promptactivity = raw_input ('Enter value for Activity. ')
	print '\n'
	print '0 = Absent '
	print '1 = Weak, irregular, gasping '
	print '2 = Strong cry '
	print '\n'
	promptrespiration = raw_input ('Enter value for respiration. ')
	print '\n'
	try:
		apgarscore = str(int(promptcomplexion) + int(promptpulsescore) + int(promptgrimace) + int(promptactivity) + int(promptrespiration)) + ' is the APGAR score. '
		print str(apgarscore)
	except:
		print 'Please enter valid integers when prompted.\n'
	print '\n'
	return
