# Welcome to sturdy-robot! This is a short script written to help EMS practitioners with various formulae that they won't be bothered to remember.
# More formulae will be added in the future.
print 'Welcome to sturdy-robot.'
print '\n'
import returnmenu
##########################################################################################
# Assign variables to the defined functions to easily add new scripts to the menu function.
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8
j = 9
k = 10
l = 11
m = 12
n = 13
o = 14
p = 15
#########################################################################################
# User Menu
# Be sure to change the integer in the if statement that runs Menu() on wrong input to 1 point above the highest numbered menu item.
def Menu():
	print 'Directory: '
	print '\n'
	print 'Parkland Formula = 0 '
	print 'Oxygen Tank Calculation = 1 '
	print 'IV Flow Rate = 2 '
	print 'Rule of Nines = 3 '
	print 'Mean Arterial Pressure = 4 '
	print 'Kg/lbs Converter = 5 '
	print 'Milligram/Microgram Converter = 6 '
	print 'Glasgow Coma Scale = 7 '
	print 'APGAR Test = 8 '
	print 'kPA/PSI Converter = 9 '
	print 'Pediatric Vitals = 10 '
	print 'PHI Score = 11 '
	print 'Cincinnati Pre Hospital Stroke Scale = 12'
	print 'Centimeter/Feet Converter = 13'
	print "Beck's Triad = 14"
	print "Cushing's Triad = 15"
	print '\n'
	try:
		promptscript = -1
		promptscript = raw_input ('Enter the number corresponding to the function you would like to run. ')
		print '\n'
		if int(promptscript) == int(a) :
			import parkland
			returnmenu.backtomenu()
		elif int(promptscript) == int(b):
			import oxygencalc
			returnmenu.backtomenu()
		elif int(promptscript) == int(c):
			import ivflowrate
			returnmenu.backtomenu()
		elif int(promptscript) == int(d):
			import ruleofnines
			returnmenu.backtomenu()
		elif int(promptscript) == int(e):
			import meanarterial
			returnmenu.backtomenu()
		elif int(promptscript) == int(f):
			import kgtolbs
			returnmenu.backtomenu()
		elif int(promptscript) == int(g):
			import mgconvert
			returnmenu.backtomenu()
		elif int(promptscript) == int(h):
			import glasgowcoma
			returnmenu.backtomenu()
		elif int(promptscript) == int(i):
			import apgar
			returnmenu.backtomenu()
		elif int(promptscript) == int(j):
			import kpatopsi
			returnmenu.backtomenu()
		elif int(promptscript) == int(k):
			import pedvitals
			returnmenu.backtomenu()
		elif int(promptscript) == int(l):
			import prehospitalindex
			returnmenu.backtomenu()
		elif int(promptscript) == int(m):
		    import cincinnati
		    returnmenu.backtomenu()
       		elif int(promptscript) == int(n):
		    import height
                    returnmenu.backtomenu()
		elif int(promptscript) == int(o):
                    import beckstriad
		    returnmenu.backtomenu()
	        elif int(promptscript) == int(p):
		    import cushingstriad
		    returnmenu.backtomenu()
		elif str(promptscript) or int(promptscript) <= -1 or int(promptscript) >= 16:
			#Needs to bring returnmenu script
			returnmenu.backtomenu()
	except ValueError:
		print 'Please enter a valid integer. '
		returnmenu.backtomenu()
Menu()
##########################################################################################
import sys
sys.exit()
