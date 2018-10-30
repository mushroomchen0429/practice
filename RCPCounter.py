import threading
import datetime
import os

global count
count = 0

def counter_timer():
    
    global timer
    global count
    timer = threading.Timer(1, counter_timer)
    timer.start()
    
    count += 1
    if (count == 120):#rollcall time per once :180
        timer.cancel()
        sendoff_timer()
        

def sendoff_timer():
    global count
    print('sendoff' + str(datetime.datetime.now()))
    os.system("python sendoff.py")
    count = 0

def total_timer():
    print('send' + str(datetime.datetime.now()))
    os.system("python send.py")
    timer3 = threading.Timer(300, total_timer)#rollcall frequency :600s
    timer3.start()
    counter_timer()

total_timer()
