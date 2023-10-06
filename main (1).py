#1.2 Write a program that determines wheather a year entered by the user is a leap year or not using ifelif-else statement
def isLeapYear (year):
  if (year%4==0 and year%100!=0) or year%400==0:
     return True
  else:
     return False
Year=int (input ("Enter a year:"))
if isLeapYear (Year):
  print("{} is a LeapYear.".format(Year))
else:
   print ("{} is not a LeapYear.".format (Year))