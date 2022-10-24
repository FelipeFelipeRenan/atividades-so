import threading 
from random import randint
import time
import random

sem = threading.Semaphore(3)

def atender(i : str):
    sem.acquire()
    print(f'Atendimento n° {i}')
    time.sleep(random.randint(3,10))
    sem.release()



threadsList = []
for i in range(0,30):
    threadsList.append(threading.Thread(target=atender, args=(i,)))
    threadsList[i].start()
for i in threadsList:
    i.join()

