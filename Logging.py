#MultiProcessing Tutorial
#https://www.youtube.com/watch?v=KpDKpgzvmrY&list=PL5tcWHG-UPH3SX16DI6EP1FlEibgxkg_6&index=4

#Video 4: Logging
#We briefly cover the logging component of the multiprocessing module

import time
import logging
from multiprocessing import Process, Lock, Value
from multiprocessing import log_to_stderr, get_logger

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

    #Instantiate logger
    #Print out all the logging information to the terminal
    log_to_stderr() 

    #Create a logger object 
    logger=get_logger()

    #Telling the logger what level we want to see the information at
    logger.setLevel(logging.INFO) 

    add_process = Process(target=add_500_lock, args=(total,lock))
    sub_process = Process(target=sub_500_lock, args=(total,lock))
    
    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()

    print(total.value)

#LOOK AT THIS CODE AROUND 7:58
