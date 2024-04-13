from threading import Thread
import random
import time

def printer(msg:str, max_sleep: int):
    for i in range(10):
        sleep_interval = random.randint(1, max_sleep)
        time.sleep(sleep_interval)
        print(msg, end = '', flush = True)

t1 = Thread(target=printer, args=('A', 10))
t2 = Thread(target=printer, args=('B', 5))
t3 = Thread(target=printer, args=('C', 15))
t4 = Thread(target=printer, args=('D', 7))
t5 = Thread(target=printer, args=('E', 2))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

