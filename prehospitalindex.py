# Prehospital Index
def prehospitalindex():
	print 'Prehospital Index as used by AHS. '
	print '\n'
	promptpressure = raw_input ('Enter blood pressure. ')
	print '\n'
	promptpulse = raw_input ('Enter pulse. ')
	print '\n'
	promptLOC = raw_input ('Level of Consciousness: 1 = Normal | 2 = Confused/Combative | 3 = No intelligible words. ')
	print '\n'
	promptresp = raw_input ('Respiratory rate: 1 = Normal | 2 = Labored | 3 = <10/min. ')
	print '\n'
	prompttrauma = raw_input ('Any penetrating wounds to head, chest, abdomen? 1 = Yes | 0 = No ')
	print '\n'
	if int(promptpressure) >= 100:
		pressurescore = 0
	elif int(promptpressure) >= 86 and int(promptpressure) <100:
		pressurescore = 1
	elif int(promptpressure) >=75 and int(promptpressure) <=85:
		pressurescore = 2
	elif int(promptpressure) >= 0 and int(promptpressure) <=74:
		pressurescore = 5
	if int(promptpulse) >= 120:
		pulsescore = 3
	elif int(promptpulse) >= 51 and int(promptpulse) <= 119:
		pulsescore = 0
	elif int(promptpulse) <= 50:
		pulsescore = 5
	if int(promptLOC) == 1:
		locscore = 0 
	elif int(promptLOC) == 2:
		locscore = 3
	elif int(promptLOC) == 3:
		locscore = 5
	if int(promptresp) == 1:
		respscore = 0
	elif int(promptresp) == 2:
		respscore = 3
	elif int(promptresp) == 3:
		respscore = 5
	if int(prompttrauma) == 1:
		traumascore = 4
	elif int(prompttrauma) == 0:
		traumascore = 0
	totalscore = (int(pressurescore) + int(pulsescore) + int(locscore) + int(respscore) + int(traumascore))
	if int(totalscore) <= 3:
		print 'PHI is ' + str(int(totalscore)) + ' | Minor Trauma '
	elif int(totalscore) >= 4:
		print 'PHI is ' + str(int(totalscore)) + ' | Major Trauma '
	print '\n'
def goback():
	promptgoback = raw_input ('Return to PHI calculator = 1 | Menu = 2 ')
	print '\n'
	if int(promptgoback) == 1:
		prehospitalindex()
	elif int(promptgoback) == 2:
		return
	else:
		return
