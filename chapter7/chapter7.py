import re
inputDate=input('Enter Date in DD/MM/YYYY: ')
date=re.compile(r'([0-3]\d)/([01]\d)/([1-2]\d\d\d)')