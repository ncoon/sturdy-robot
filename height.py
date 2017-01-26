# Height conversion for cm to ft and vice-versa
def height():
    promptconvert = raw_input ('Do you want to convert ft>cm = 1 or cm>ft = 2?')
    print "\n"
    if int(promptconvert) == 1:
        promptfeet = raw_input ("Enter patient's height in feet.")
        fttocm = (float(promptfeet) * 30.48)
        print "Patient's height is " + str(float(fttocm)) + " cm .\n"
    elif int(promptconvert) == 2:
        promptcm = raw_input ("Enter patient's height in centimeters.")
        cmtoft = ((float(promptcm) * 0.394) / 12)
        print "Patient's height is " + str(float(cmtoft)) + " ft.\n"
    promptgoback = raw_input ('Go back to calculator? 1 = Yes | 0 = No ')
    print "\n"
    if str(promptgoback) == '':
        return
    elif int(promptgoback) < 1 or int(promptgoback) >= 2:
        return
    elif int(promptgoback) == 1:
        height()
    elif int(promptgoback) == 0:
        return
height()
