from datetime import datetime
from datetime import date
now = datetime.now() # current date and time
print(now)
print(type(now))
year = now.strftime("%Y")
print(year)
print(type(year))
today = date.today()
print(today)
dates = today.strftime('%d-%m-%Y')
print(type(today))
print(dates)
print(type(dates))
