import calendar
import datetime

def Jan_Attendance(month,year):

    month=1
    year=2020

    weekday,lastday=calendar.monthrange(year,month)
    attendance=list(range(1,lastday+1))
    holidays=[(13,'Lohri','Holiday'),(26,'Republic Day','Holiday')]
    absent=[(10,'Absent','NA'),(15,'Leave','Fever')]

    #Fill Attendance by default Present 
    for i in range(lastday):
        attendance[i]=(i+1,'Present','-------') 
    #Update All Absents and Leave
    for abs in absent:
        day = abs[0]
        attendance[day-1]=abs

    #Update All Saturday and Sunday
    for i in range(1,lastday):
        day = datetime.datetime(year,month,i).strftime("%A")
        if day =="Saturday" or day == "Sunday":
            attendance[i-1]=(i,day,'weekoff')

    #Update All Holidays
    for hday in holidays:
        day = hday[0]
        attendance[day-1]=hday

    # print("Month List : ",attendance)
    # print("Attendance Start")
    # for day in attendance:
    #     print(day)

    return (attendance,weekday,lastday)    