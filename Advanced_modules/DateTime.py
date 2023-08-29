import datetime

print("Basics of datetime: ")
mytime = datetime.time(2, 20)
print("Minute in mytime is {}min".format(mytime.minute))
print("Hour in mytime is {}hr".format(mytime.hour))
print("Time in mytime is {}".format(mytime))
print("Microseconds in my time is {}".format(mytime.microsecond))

print("\nPrecise time:")
precisetime = datetime.time(13, 20, 1, 20)
print("Current time is {}".format(precisetime))
print("Type of datetime is {}".format(type(precisetime)))

print("\nBasics of dates: ")
today = datetime.date.today()
print("Todays date is {}".format(today))
print("This year is {}, month is {}, date is {}".format(today.year, today.month, today.day))
print("Todays day with date and time is {}".format(today.ctime()))


from datetime import datetime

print("\nCombining date, time")
# datetime(year, month, date, hour, minute, second)
mydatetime = datetime(2021, 10, 3, 14, 20, 1)
print("date time in mydatetime is {}".format(mydatetime))

print("\nReplacing date time")
mydatetime = mydatetime.replace(year=2020)
print("New date time in mydatetime is {}".format(mydatetime))


from datetime import date

print("\nLenth between 2 dates")
date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
result = date1 - date2
print("Type of result is {}".format(type(result)))
print("Duration between date1 and date2 is {}".format(result.days))

print("\nLenth between 2 datetime")
datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)
mydiff = datetime1 - datetime2
print("Duration between datetime1 and datetime2 is {}".format(mydiff))
print("Hours between datetime1 and datetime2 is {}".format(mydiff.seconds/60/60))
print("Total Hours between datetime1 and datetime2 is {}".format(mydiff.total_seconds()/60/60))





