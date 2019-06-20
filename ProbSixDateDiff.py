import datetime

year1=int(input("enter year for date1"))
month1=int(input("enter month for date1"))
day1=int(input("enter day for date1"))
#print(datetime.datetime(year1,month1,day1))
year2=int(input("enter year for date2"))
month2=int(input("enter month for date2"))
day2=int(input("enter day for date2"))

d3=datetime.datetime(year2,month2,day2)-datetime.datetime(year1,month1,day1)
print(d3)