# An extra day is added to the calendar almost every four years as
# February 29, and the day is called a leap day. A leap year contains a leap
# day.
# These are the conditions used to identify leap years:
# if the year can be evenly divided by 4, it is then a leap year
# but if the year is evenly divided by 4 and also by 100, then it is NOT a
# leap year
# but if the year is evenly divided by 4 and also by 400, then it is a leap
# year
# This means the years 2000 and 2400 are leap years, while 1800, 1900,
# 2100, 2200, 2300 and 2500 are NOT leap years.
# Ask a year input from user. And tell if the year entered by user is leap or
# not


def leap(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print("Leap")
    else:
        print("Not Leap")


leap(2200)
