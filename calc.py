import time
import datetime

def isValidTransactionDate(date):

	nowstring = time.strftime('%Y %m %d')
	nowstring = nowstring.split(' ')
	dtnow = datetime.datetime(int(nowstring[0]), int(nowstring[1]), int(nowstring[2]))

	try:
		datelist = date.split('/')
		dtdate = datetime.datetime(int(datelist[2]), int(datelist[1]), int(datelist[0]))
	except: dtdate = None

	if dtdate != None and dtdate >= dtnow: return True
	else: return False
