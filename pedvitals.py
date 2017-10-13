# Average Pediatric Weights and Vital Signs
def pedvitals():
	print 'Average weights and vitals signs by age. '
	print '\n'
	promptage = float(raw_input('Enter patient age in years. \n' '(If <1 year enter either 0(for birth), 0.25(3 months) or 0.5(6 months)) \n'))
	birth = 'Weight = 3 kg, IV Bolus = 70ml, ET Size = 3.0, Pulse = 100-160, Resp = 30-60, BP = 65-90/45-65 '
	threemonths = 'Weight = 5 kg, IV Bolus = 100ml, ET Size = 3.5, Pulse = 100-160, Resp = 30-60, BP = 65-90/45-65 '
	sixmonths = 'Weight = 7 kg, IV Bolus = 140ml, ET Size = 3.5, Pulse = 100-160, Resp = 24-30, BP = 65-90/45-65 '
	oneyear = 'Weight = 10 kg, IV Bolus = 200ml, ET Size = 4.0, Pulse = 70-120, Resp = 24-30, BP = 80-100/55-65 '
	twoyear = 'Weight = 12 kg, IV Bolus = 240ml, ET Size = 4.5, Pulse = 70-120, Resp = 20-30, BP = 90-110/55-75 '
	threeyear = 'Weight = 15 kg, IV Bolus = 300ml, ET Size = 4.5, Pulse = 70-120, Resp = 20-30, BP = 90-110/55-75 '
	fouryear = 'Weight = 17 kg, IV Bolus = 340ml, ET Size = 5.0, Pulse = 70-120, Resp = 20-30, BP = 90-110/55-75 '
	fiveyear = 'Weight = 18 kg, IV Bolus = 360ml, ET Size = 5.0, Pulse = 70-120, Resp = 20-30, BP = 90-110/55-75 '
	sixyear = 'Weight = 20 kg, IV Bolus = 400ml, ET Size = 5.5, Pulse = 70-120, Resp = 12-20, BP = 90-110/55-75 '
	eightyear = 'Weight = 25 kg, IV Bolus = 500ml, ET Size = 6.0, Pulse = 70-120, Resp = 12-20, BP = 90-110/55-75 '
	tenyear = 'Weight = 30 kg, IV Bolus = 600ml, ET Size = 6.5, Pulse = 70-120, Resp = 12-20, BP = 90-110/55-75 '
	twelveyear = 'Weight = 38 kg, IV Bolus = 760ml, ET Size = 7.0, Pulse = 60-100, Resp = 12-20, BP = 110-135/65-85 '
	overtwelve = 'IV Bolus = 20ml/kg, ET Size = (16+age(Years))/4, Pulse 60-100, Resp = 12-20, BP = 80 + 2X Age(Years) (Systolic)'
	try:
		if int(promptage) == 0:
			print '\n'
			print birth
		elif float(promptage) >= 0.25 and float(promptage) < 0.5:
			print '\n'
			print threemonths
		elif float(promptage) >= 0.5 and float(promptage) < 1:
			print '\n'
			print sixmonths
		elif int(promptage) == 1:
			print '\n'
			print oneyear
		elif int(promptage) == 2:
			print '\n'
			print twoyear
		elif int(promptage) == 3:
			print '\n'
			print threeyear
		elif int(promptage) == 4:
			print '\n'
			print fouryear
		elif int(promptage) == 5:
			print '\n'
			print fiveyear
		elif int(promptage) == 6:
			print '\n'
			print sixyear
		elif int(promptage) == 7 or int(promptage) == 8:
			print '\n'
			print eightyear
		elif int(promptage) == 9 or int(promptage) == 10:
			print '\n'
			print tenyear
		elif int(promptage) == 11 or int(promptage) == 12:
			print '\n'
			print twelveyear
		elif int(promptage) > 12 and int(promptage) <=17:
			print '\n'
			print overtwelve
		elif int(promptage) >= 18:
			print '\n'
			print 'Please reference adult vitals charts. '
	except:
		print 'Please enter an integer in the range of 0 through 18. '
	print '\n'
	print 'Source: https://myhealth.alberta.ca/Health/Pages/conditions.aspx?hwid=abo2987 '
	print '\n'
	print '\n'

def goback():
	promptgoback = raw_input ('Return to Pediatric Vitals = 1 | or Menu = 2 ')
	if int(promptgoback) == 1:
		pedvitals()
	elif int(promptgoback) >= 2:
		return

