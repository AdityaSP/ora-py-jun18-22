from threading import Thread, Lock
import time
a = 0

def counter():
    time.sleep(1)
    global a
    l.acquire()
    c = a
    time.sleep(1)
    c = c + 1
    a =c
    print a
    l.release()

l = Lock()
for i in range(5):
    th = Thread(target=counter)
    th.start()
