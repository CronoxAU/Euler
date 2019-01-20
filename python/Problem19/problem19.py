#Solution to Project Euler problem 19 - https://projecteuler.net/problem=19
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime
#create a function to find the day of the week for a given date
#loop through the selected timeframe checking for days of the specified type

#returns the day of the week as a numeral in the with the following values:
# 0 = Monday
# 1 = Tuesday
# 2 = Wednesday
# 3 = Thursday
# 4 = Friday
# 5 = Saturday
# 6 = Sunday
def day_of_week(y, m, d):
  return datetime.date(y, m, d).weekday()

#returns the number of sundays that fell on the first day of the month during the given date range
def sundaysOnFirstDay(startYear, endYear):
  sum = 0
  for year in range(startYear,endYear + 1):
    for month in range (1,13):
      if(day_of_week(year, month, 1) == 6):
        sum += 1
  return sum