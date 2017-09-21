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
q = 16
r = 17
#########################################################################################
# User Menu
# Be sure to change the integer in the if statement that runs Menu() on wrong input to 1 point above the highest numbered menu item.
def Menu():
	infinitemenu = 102
	while infinitemenu == 102:
		try:
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
			print "Dieulafoy's Triad = 16"
			print "Reynold's Pentad = 17"
			print '\n'

			promptscript = -1
			promptscript = raw_input ('Enter the number corresponding to the function you would like to run. ')
			print '\n'
			if int(promptscript) == int(a) :
				import parkland
				parkland.parkland()
				returnmenu.backtomenu()
			elif int(promptscript) == int(b):
				import oxygencalc
				oxygencalc.oxygencalc()
				returnmenu.backtomenu()
			elif int(promptscript) == int(c):
				import ivflowrate
				ivflowrate.ivflowrate()
				returnmenu.backtomenu()
			elif int(promptscript) == int(d):
				import ruleofnines
				ruleofnines.ruleofnines()
				returnmenu.backtomenu()
			elif int(promptscript) == int(e):
				import meanarterial
				meanarterial.meanarterial()
				returnmenu.backtomenu()
			elif int(promptscript) == int(f):
				import kgtolbs
				kgtolbs.kgtolbs()
				kgtolbs.goback()
				returnmenu.backtomenu()
			elif int(promptscript) == int(g):
				import mgconvert
				mgconvert.mgconvert()
				mgconvert.goback()
				returnmenu.backtomenu()
			elif int(promptscript) == int(h):
				import glasgowcoma
				glasgowcoma.glasgowcoma()
				returnmenu.backtomenu()
			elif int(promptscript) == int(i):
				import apgar
				apgar.apgar()
				returnmenu.backtomenu()
			elif int(promptscript) == int(j):
				import kpatopsi
				kpatopsi.kpatopsi()
				kpatopsi.goback()
				returnmenu.backtomenu()
			elif int(promptscript) == int(k):
				import pedvitals
				pedvitals.pedvitals()
				pedvitals.goback()
				returnmenu.backtomenu()
			elif int(promptscript) == int(l):
				import prehospitalindex
				prehospitalindex.prehospitalindex()
				returnmenu.backtomenu()
			elif int(promptscript) == int(m):
				import cincinnati
				cincinnati.cincinnati()
			    	returnmenu.backtomenu()
			elif int(promptscript) == int(n):
				import height
				height.height()
				height.goback()
                	    	returnmenu.backtomenu()
			elif int(promptscript) == int(o):
                	    	import beckstriad
				beckstriad.beckstriad()
			    	returnmenu.backtomenu()
	        	elif int(promptscript) == int(p):
			    	import cushingstriad
				cushingstriad.cushingstriad()
			    	returnmenu.backtomenu()
			elif int(promptscript) == int(q):
			    	import dieulafoystriad
				dieulafoystriad.dieulafoystriad()
			    	returnmenu.backtomenu()
			elif int(promptscript) == int(r):
			    	import reynoldspentad
				reynoldspentad.reynoldspentad()
			    	returnmenu.backtomenu()
			elif str(promptscript) or int(promptscript) <= -1 or int(promptscript) >= 18:
				#Needs to bring returnmenu script. REMEMBER to change the integer to a value greater than the highest numbered script.
				returnmenu.backtomenu()
		except ValueError:
			print 'Please enter a valid integer. '
			returnmenu.backtomenu()
Menu()
##########################################################################################
import sys
sys.exit()
