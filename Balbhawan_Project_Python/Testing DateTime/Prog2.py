import datetime
import calendar
day,month,year="10/2/2019".split("/")
print(type(year))
print("Year : ",year)
weekday,lastday=calendar.monthrange(int(year),int(month))
print("Last Day of Month",lastday)

monthList=list( range(1,lastday+1))
print("Month List : ",monthList)


ab1="10/01/2020"
ab2="15/01/2020"
sat=""

attendance=[]
tp_present=("1","Present","----")
tp_saturday=("-----","Saturday","----")
tp_sunday=("-----","Sunday","----")
tp_holiday=("14","Makar","Holiday")

