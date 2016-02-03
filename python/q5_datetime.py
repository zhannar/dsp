# Hint:  use Google to find python function

def diff_time(date_start, date_stop, date_format):
	#This is a function which takes a start date, an end date, 
	# and a particular date format to calculate the number of days 
	#in between them.
	from datetime import datetime
	a = datetime.strptime(date_start, date_format)
	b = datetime.strptime(date_stop, date_format)
	delta = b - a
	return delta.days


####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

date_format = "%m-%d-%Y"

difference = diff_time(date_start,date_stop,date_format);

print "Part a: The number of days between %s and %s is %s days." % (date_start, date_stop, difference)

####b)  
date_start = '12312013'
date_stop = '05282015' 

date_format = "%m%d%Y"

difference = diff_time(date_start,date_stop,date_format);

print "Part b: The number of days between %s and %s is %s days." % (date_start, date_stop, difference)

####c)  

date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_format = "%d-%b-%Y"
# Note: '%b' is the abbreviated month name

difference = diff_time(date_start,date_stop,date_format);

print "Part c: The number of days between %s and %s is %s days." % (date_start, date_stop, difference)

#Referemces:
#http://stackoverflow.com/questions/151199/how-do-i-calculate-number-of-days-betwen-two-dates-using-python
# http://www.tutorialspoint.com/python/time_strptime.htm