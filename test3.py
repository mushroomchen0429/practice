import datetime
import threading

global sec
sec = 10

def run_before(lastfunc, *args1, **kwargs1):
    def run(func):
        def wrapped_func(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except:
                result = None
            finally:
                lastfunc(*args1, **kwargs1)
                return result
        return wrapped_func
    return run


def sendoff():
    print("Sendoff" + str(datetime.datetime.now()))
    print(" ")
    time = threading.Timer(2, sendoff)
    time.start()


@run_before(sendoff)
def send():
    print("Send" + str(datetime.datetime.now()))
    # print (" ")
    global time
    time = threading.Timer(5, send)
    time.start()

send()
