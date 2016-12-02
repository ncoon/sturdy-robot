# IV Flow Rate Calc
# (Volume / time(minutes)) * (drop factor / 1)
def IVFlowRate():
	prompttotal = raw_input ('Enter the total volume to be administered. (Milliliters) ')
	print '\n'
	prompttime = raw_input ('Enter the time the volume is to be administered in. (Minutes only) ')
	print '\n'
	promptdrop = raw_input ('Enter the drop factor. (Example: 10) ')
	print '\n'
	dropspermin = ((int(prompttotal) / int(prompttime)) * (int(promptdrop) / 1))
	dropsper10s = (int(dropspermin) / 6)
	print str(int(dropspermin)) + ' Drops per minute. Or ' + str(int(dropsper10s)) + ' drops per 10 seconds. '
	print '\n'
	return
IVFlowRate()
