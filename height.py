# Height conversion for cm to ft and vice-versa
def height():
    promptconvert = eval(input ('Do you want to convert ft>cm = 1 or cm>ft = 2?'))
    print("\n")
    if int(promptconvert) == 1:
        promptfeet = eval(input ("Enter patient's height in feet."))
        fttocm = (float(promptfeet) * 30.48)
        print(("Patient's height is " + str(float(fttocm)) + " cm .\n"))
    elif int(promptconvert) == 2:
        promptcm = eval(input ("Enter patient's height in centimeters."))
        cmtoft = ((float(promptcm) * 0.394) / 12)
        print(("Patient's height is " + str(float(cmtoft)) + " ft.\n"))
def goback():
	promptgoback = eval(input ('Go back to calculator? 1 = Yes | 0 = No '))
	print("\n")
	if int(promptgoback) < 1 or int(promptgoback) >= 2:
		return
	elif int(promptgoback) == 1:
        	height()
	elif int(promptgoback) == 0:
        	return
	else :
		return
