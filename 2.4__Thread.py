import time
import threading
def printTimeOnceASecond():
    print(time.asctime())
    time.sleep(1)
# for i in range(10):
#     printTimeOnceASecond()
    
class testThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        for i in range(10):
            print(self.name)
            printTimeOnceASecond()
t1 = testThread(1,"t1",1)
t2 = testThread(2,"t2",2)
t1.start()
t2.start()

t1.join()
t2.join()
    
