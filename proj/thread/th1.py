import time
import threading
import random

def heavyduty(num):
    print "Started" + str(num)
    time.sleep(random.randint(1,5))
    print "Finished" + str(num)

th_list = []
for i in range(5):
    t = threading.Thread(target=heavyduty, args=(i,))
    th_list.append(t)
    t.start()

time.sleep(1)
print map(lambda x : x.is_alive(), th_list)
print threading.active_count()
time.sleep(1)
print map(lambda x : x.is_alive(), th_list)
print threading.active_count()
time.sleep(1)
print map(lambda x : x.is_alive(), th_list)
print threading.active_count()


# t1 = threading.Thread(target=heavyduty, args=(0,))
# t2 = threading.Thread(target=heavyduty, args=(1,))
# t3 = threading.Thread(target=heavyduty, args=(2,))
# t4 = threading.Thread(target=heavyduty, args=(3,))
# t5 = threading.Thread(target=heavyduty, args=(4,))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()

#heavyduty(0)
#heavyduty(1)
#heavyduty(2)
#heavyduty(3)
#heavyduty(4)

