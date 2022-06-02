import datetime

'''
year = int(input('vvedite god '))
month = int(input('vvedite mesiats '))
day = int(input('vvedite den '))

date_object = datetime.datetime(year, month, day)
date_today = datetime.datetime.today()
delta = date_today - date_object
print(delta)
'''

'''
year_start = int(input('vvedite god pervoi daty '))
month_start = int(input('vvedite mesiats pervoi daty '))
day_start = int(input('vvedite den pervoi daty '))

year_end = int(input('vvedite god vtoroi daty '))
month_end = int(input('vvedite mesiats vtoroi daty '))
day_end = int(input('vvedite den vtoroi daty '))

date_first = datetime.datetime(year_start, month_start, day_start)
date_fin = datetime.datetime(year_end, month_end, day_end)
delta = date_fin - date_first
print(delta)
'''

now = datetime.datetime.now()
year = datetime.datetime.strftime(now,'%B')
print(year)
