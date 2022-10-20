import datetime

# x = datetime.datetime.now()
strDate="10/10/2020"
day,month,year=strDate.split("/")

print("Day : ",day)
print("Month : ",month)
print("Year : ",year)
x = datetime.datetime(int(year),int(month),int(day))
print(x.year)
print(x.month)
print(x.strftime("%B"))
print(x.strftime("%A"))