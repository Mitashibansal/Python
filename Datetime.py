import datetime 
from datetime import date
x = datetime.datetime.now()
x= datetime.date(2021,6,6)
print(x.strftime("%W"))
print(x.strftime("%w"))
