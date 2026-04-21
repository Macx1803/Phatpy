from datetime import datetime
now = datetime.now()
print(now.year)
print(now.strftime("%B"))
print(now.strftime("%U"))
day_of_month = now.day
week_of_month = (day_of_month - 1)// 7+1
print(week_of_month)
print(now.strftime("%j"))
print(now.day)
print(now.strftime("%A")) 
print(now.strftime("%H:%M:%S"))