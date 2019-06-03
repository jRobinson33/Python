#DateTime tutorial
#6/3/2019

import datetime

#datetime constructor requires 3 inputs, year, month, day
gvr = datetime.date(1956, 1, 31)

print("accessing the year month and day of gvr variable")
print(gvr.year)
print(gvr.month)
print(gvr.day)

#you can add a time delta to a date to get the new date
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100) #dt deltatime
print(mill + dt)

#you can change the format of the date
""" formatting codes
%a: Returns the first three characters of the weekday, e.g. Wed.
%A: Returns the full name of the weekday, e.g. Wednesday.
%B: Returns the full name of the month, e.g. September.
%w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
%m: Returns the month as a number, from 01 to 12.
%p: Returns AM/PM for time.
%y: Returns the year in two-digit format, that is, without the century. For example, "18" instead of "2018".
%f: Returns microsecond from 000000 to 999999.
%Z: Returns the timezone.
%z: Returns UTC offset.
%j: Returns the number of the day in the year, from 001 to 366.
%W: Returns the week number of the year, from 00 to 53, with Monday being counted as the first day of the week.
%U: Returns the week number of the year, from 00 to 53, with Sunday counted as the first day of each week.
%c: Returns the local date and time version.
%x: Returns the local version of date.
%X: Returns the local version of time.
"""
#demonstrating the use of the strftime formatting codes
print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)

print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)

print(launch_datetime.year)
print(launch_datetime.month)
print(launch_datetime.day)
print(launch_datetime.hour)
print(launch_datetime.minute)
print(launch_datetime.second)

now = datetime.datetime.today()
print(now)
print(now.microsecond)


#This bottom section seems to cause a EOF parsing error, perhaps it was meant for python 2
#moon_landing = "7/20/1969"
#moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
#print(moon_landing_datetime)
#print(type(moon_landing_datetime)