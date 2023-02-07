# Calculates weight based dosages and total volume of drug to administer.
def dosagecalc():
	try:
		asksolid = eval(input ('Do you want to calculate g/mg/mcg per kg (1) or volume of drug to administer (2)?\n'))
		if int(asksolid) == 1:
			askunit = eval(input ('How many g/mg/mcg per kg?\n'))
			askweight = eval(input ('Patient weight in kg?\n'))
			dosage = (float(askunit) * float(askweight))
			print(('The dose is ' + str(float(dosage)) + ' g/mg/mcg.\n'))
			gobackdosage()
		elif int(asksolid) == 2:
			askdosage = eval(input ('Dosage to be administered? (g/mg/mcg)\n'))
			askunit = eval(input ('Total amount of drug (g/mg/mcg) in the ampoule/vial/bag?\n'))
			askvolume = eval(input ('Total volume of ampoule/vial/bag? (L/mL)\n'))
			dosage = ((float(askdosage) / float(askunit)) * float(askvolume))
			print(('The volume to be administered is ' + str(float(dosage)) + ' L/mL.\n'))
			gobackdosage()
	except:
		print('Please enter a valid number.\n')
		gobackdosage()
def gobackdosage():
	try:
		promptgoback = eval(input ('Run another calculation (1) or return to menu (2)?\n'))
		if int(promptgoback) == 1:
			dosagecalc()
		elif int(promptgoback) == 2:
			return
	except:
		print('Please enter a valid number.\n')
		return
