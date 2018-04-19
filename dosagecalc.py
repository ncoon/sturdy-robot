# Calculates weight based dosages and total volume of drug to administer.
def dosagecalc():
	try:
		asksolid = raw_input ('Do you want to calculate g/mg/mcg per kg (1) or volume of drug to administer (2)?\n')
		if int(asksolid) == 1:
			askunit = raw_input ('How many g/mg/mcg per kg?\n')
			askweight = raw_input ('Patient weight in kg?\n')
			dosage = (float(askunit) * float(askweight))
			print 'The dose is ' + str(float(dosage)) + ' g/mg/mcg.\n'
			gobackdosage()
		elif int(asksolid) == 2:
			askdosage = raw_input ('Dosage to be administered? (g/mg/mcg)\n')
			askunit = raw_input ('Total amount of drug (g/mg/mcg) in the ampoule/vial/bag?\n')
			askvolume = raw_input ('Total volume of ampoule/vial/bag? (L/mL)\n')
			dosage = ((float(askdosage) / float(askunit)) * float(askvolume))
			print 'The volume to be administered is ' + str(float(dosage)) + ' L/mL.\n'
			gobackdosage()
	except:
		print 'Please enter a valid number.\n'
		gobackdosage()
def gobackdosage():
	try:
		promptgoback = raw_input ('Run another calculation (1) or return to menu (2)?\n')
		if int(promptgoback) == 1:
			dosagecalc()
		elif int(promptgoback) == 2:
			return
	except:
		print 'Please enter a valid number.\n'
		return
