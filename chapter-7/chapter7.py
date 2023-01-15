import re

def datedetection(text):
  leap_Year = False
  month_Days ={'01':'31','02':'28','03':'31','04':'30','05':'31','06':'30','07':'31','08':'31','09':'30','10':'31','11':'30','12':'31'}
  
  date = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{1,4})')

  result = (date.findall(text))
  for i in range(len(result)):
    day, month, year = result[i]

    if month not in month_Days.keys(): 
      return 'Invalid month'
    if int(year) % 4 == 0: 
      leap_Year = True
      if int(year) % 100 == 0 and int(year) % 400 != 0:
        leapYear = False

    if leap_Year:
      month_Days['02'] = '29'
    if month_Days[month] < day: 
      return 'Invalid date'

  return 'Valid Date'    
x=input("Enter the date u want to check in format dd/mm/yy")

print(datedetection(x))