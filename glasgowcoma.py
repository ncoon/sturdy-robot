def GlasgowComaScale():
	print 'Eyes - 1 = Does not open eyes | 2 = Opens eyes in response to pain '
	print '3 = Opens eyes in response to voice | 4 = Opens eyes spontaneously '
	print '\n'
	prompteyes = raw_input ('Enter value for Eyes. ')
	print '\n'	
	print 'Verbal - 1 = Makes no sounds | 2 = Incomprehensible sounds ' 
	print '3 = Utters inappropriate words | 4 = Confuse, disoriented '
	print '5 = Oriented, converses normally '
	print '\n'
	promptverbal = raw_input ('Enter value for Verbal. ')
	print '\n'
	print 'Motor - 1 = Makes no movements | 2 = Extension to painful stimuli (decerebrate) ' 
	print '3 = Abnormal Flexion to painful stimuli (decorticate) | 4 = Flexion / Withdrawal to painful stimuli '
	print '5 = Localizes painful stimuli | 6 = Obeys commands '
	print '\n'
	promptmotor = raw_input ('Enter value for Motor. ')
	print '\n'
	totalgcs = int(prompteyes) + int(promptverbal) + int(promptmotor)
	print 'Total GCS score = ' + str(int(totalgcs)) + '. '
	print '\n'
	return
GlasgowComaScale()
