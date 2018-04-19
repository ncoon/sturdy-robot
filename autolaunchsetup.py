import os.rename
def autolaunchsetup(): # This moves the auto launch script to ~/.termux/boot
	try:
		promptuser = raw_input ('Do you want sturdyrobot to launch when termux starts? 1 = Yes | 0 = No\n')
		if int(promptuser) == 1:
			os.rename("~/sturdyrobotauto.sh", "~/.termux/boot/sturdyrobotauto.sh")
			print 'It is done.\n'
			return
		elif int(promptuser) == 0:
			print 'Did nothing.\n'
			return
	except:
		print 'Doing nothing, to try again, re run the initialsetup.sh\n'
		print 'Please enter either 1 or 0.\n'
		return
autolaunchsetup()
