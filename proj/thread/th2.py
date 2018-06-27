import threading
import time

a = None

def consumer():
    print "Consumer: up"
    time.sleep(10)
    print "Consumer: May be I have to wait"
    e.wait()
    print "Consuming a:", a

def publisher():
    print "Publisher: up"
    time.sleep(20)
    global a
    a = 100
    print "Pubisher: I have not set the value"
    print "Publisher: Consumer, you can proceed now"
    e.set()

e = threading.Event()

ct = threading.Thread(target=consumer)
pt = threading.Thread(target=publisher)

ct.start()
pt.start()
