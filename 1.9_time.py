#import time
import time
#return a float
currentTime = time.time()
print(currentTime)
#get a time tuple
localCurrentTime=time.localtime()
print(localCurrentTime)
print(localCurrentTime.tm_year)
print(localCurrentTime.tm_mon)
print(localCurrentTime.tm_mday)
print(localCurrentTime.tm_hour)
print(localCurrentTime.tm_min)
print(localCurrentTime.tm_sec)
print(localCurrentTime.tm_wday)
print(localCurrentTime.tm_yday)
print(localCurrentTime.tm_isdst)
#get a formatted time
ascLocalCurrentTime = time.asctime()
print(ascLocalCurrentTime)
