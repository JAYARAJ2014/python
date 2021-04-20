from datetime import datetime

dt = datetime(2020, 4, 20)
dt = datetime.now()


print(dt.strftime("%Y/%m/%d"))

dt1 = datetime(1999, 08, 31)
dt2 = datetime.now()

duration = dt2-dt1
print(duration.days)
