import time
print("===========")
curTime = time.time()
print(curTime)
totalSeconds = int(curTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHour = totalMinutes // 60
currentHour = totalHour % 24
print("Current time in Greenwich is \n"\
      ,currentHour,"-",currentMinute,"-",currentSecond)
import datetime
curDate=datetime.datetime.now()
print(str(curDate.hour) + ":"+str(curDate.minute)+":"+str(curDate.hour))

