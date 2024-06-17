#MultiProcessing Tutorial
#https://youtu.be/iYJNmuD4McE?si=c-vZo9SDRg6_FziC

#Video 3: Locks
#A lock or mutex is a synchronization mechanism for enforcing
#limits on access to a resource in an environment where there 
#are many threads of execution

import time
from multiprocessing import Process, Lock, Value

def add_500_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire() 
        total.value +=5
        lock.release()
    
            
def sub_500_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -=5
        lock.release()

#Lock object makes sure the blocked off process is completed before moving onto other code

if __name__=='__main__':
    total=Value('i',500)

    lock = Lock()

    add_process = Process(target=add_500_lock, args=(total,lock))
    sub_process = Process(target=sub_500_lock, args=(total,lock))
    
    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()

    print(total.value)

#LOOK AT THIS CODE AROUND 7:58
