import datetime

year: int = input('vvedite god ')
month: int = input('vvedite mesiats ')
day: int = input('vvedite den ')

date_object = datetime.datetime(year,month,day)
print(date_object)