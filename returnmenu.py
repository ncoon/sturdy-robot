def backtomenu():
	infiniteloop = 101
	while infiniteloop == 101:
		try:
			promptmenu = -1	
			print '\n'
			promptmenu = raw_input ('Return to menu? 1 = Yes , 0 = No ')
			print '\n'
			if int(promptmenu) > 0:	
				return 
				print '\n'
			elif int(promptmenu) == 0:
				print 'See you later! '
				quit()
			if str(promptmenu) or str(promptmenu) == '' or int(promptmenu) < 0:
				print 'See you later! '
				quit()
			elif int(promptmenu) >= 2:
				print 'See you later! '
				quit()
		except ValueError:
			print 'Please enter either 1 or 0. '
