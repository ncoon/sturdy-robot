import shutil
def autolaunchsetup(): # This moves the auto launch script to ~/.termux/boot
	promptuser = raw_input ('Do you want sturdyrobot to launch when termux starts? Y/n\n')
	if str(promptuser) == 'Y':
		shutil.move("~/sturdyrobotauto.sh", "~/com.termux/boot/sturdyrobotauto.sh")
		print 'It is done.\n'
		return
	elif str(promptuser) == 'n':
		print 'Did nothing.\n'
		return
	else:
		print 'Doing nothing, to try again, re run the initialsetup.sh\n'
		print 'Please enter either Y or n.\n'
		return
autolaunchsetup()
