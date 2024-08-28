import datetime

current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

print("Month (As full name):", current_datetime.strftime("%B"))
print("Weekday (As full Name:)", current_datetime.strftime("%A"))
print("Year (As four digit):", current_datetime.strftime("%Y"))
print("Weekday (As abbreviated name):", current_datetime.strftime("%a"))
print("Year (As two digit):", current_datetime.strftime("%y"))
print("Day of the month (01-31):", current_datetime.strftime("%d"))
print("Hour (24-hour clock):", current_datetime.strftime("%H"))
print("Hour (12-hour clock):", current_datetime.strftime("%I"))
print("Minute (00-59):", current_datetime.strftime("%M"))
print("Second (00-59):", current_datetime.strftime("%S"))
print("AM/PM indicator:", current_datetime.strftime("%p"))