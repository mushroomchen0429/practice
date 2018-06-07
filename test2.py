import datetime
import threading
from threading import Thread

global time
global count
global average
count = 0
classtime = 50
part = 10
average = classtime/part

def send():
    global count
    print("開始" + str(datetime.datetime.now()))
    time = threading.Timer(10, send)
    time.start()
    count += 1
    print("開始" + str(count))
    while (count == 7):
        sendoff()

def sendoff():
    global count
    print("結束" + str(datetime.datetime.now()))
    
    print("結束" + str(count))
    print("")
    if (count == 10):
        count = 0
        send()
    count += 1
    


def test():
    global count
    #  while (count > 7):
    #     sendoff()
    send()
    

send()

# time = threading.Timer(0,send)
# time.start()    
