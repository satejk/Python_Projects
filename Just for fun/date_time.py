
#Author : SATEJ V. KHANDEPARKAR
# MASTERS IN EMBEDDED AND INTELLIGENT SYSTEMS
# HALMSTAD UNIVERSITY , sweden

# This program prints the date and time to the terminal.


from datetime import datetime
now = datetime.now()

print now

current_year = now.year
current_month = now.month
current_day = now.day

#time

h = now.hour
m = now.minute
s = now.second

print current_year
print current_month
print current_day



print str(current_month) +"/"+str(current_day)+"/"+str(current_year)
print str(h) +":"+str(m)+":"+str(s)

print str(current_month) +"/"+str(current_day)+"/"+str(current_year) +"::"+str(h) +":"+str(m)+":"+str(s)
