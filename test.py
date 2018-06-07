import datetime

import threading

global sec
sec = 10

def send():
    
    
    print ("Send" + str(datetime.datetime.now()))
    # print (" ")
    global time
    time = threading.Timer(sec, send)
    time.start()

def sendoff():
    print ("Sendoff" + str(datetime.datetime.now()))
    print (" ")
    time = threading.Timer(sec+2, sendoff)
    time.start()
    
def combine():
    send()
    sendoff()

t = threading.Timer(0,combine)
t.start()
