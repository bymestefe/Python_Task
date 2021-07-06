# -*- coding: utf-8 -*-

def isLeapYear(year):
    if(year >= 1 and year <= 9999):
        if(year % 4 == 0 and year % 100 != 0):
            return True
        elif(year % 400 == 0):
            return True
    return False
    

x = isLeapYear(12000)

if(x):
    print("Leap Year")
else:
    print("Not Leap Year")
                