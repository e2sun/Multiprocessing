#MultiProcessing Tutorial
#https://www.youtube.com/watch?v=u2jTn-Gj2Xw&list=PL5tcWHG-UPH3SX16DI6EP1FlEibgxkg_6&index=5

#Video 5: Pool
#One can create a pool of processes which will carry out tasks submitted to 
#it with the Pool class

#A process pool object which controlls a pool of worker processes to which 
#jobs can be submitted. It supports asynchronous results with timeouts and 
#callbacks and has a parallel map implementation

import multiprocessing
import time
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor

#Loop through the range of number and sum 0 to that number squared
def sum_square(number):
    s=0
    for i in range(number):
        s+=i*i
    return s

def sum_square_with_mp(numbers):

    start_time=time.time()

    #Creating a pool object
    p=Pool()

    #Take a function and a list of iterable and maps all of the iterables of the function onto the processors of the machine
    result=p.map(sum_square, numbers)
    print(result)

    p.close()
    p.join()

    end_time = time.time()-start_time
    
    print("Processing " + str(len(numbers)) + " numbers took " + str(end_time) + " time using Pool from multiprocessing.")


def sum_square_no_mp(numbers):
    start_time=time.time()
    result=[]
    for i in numbers:
        result.append(sum_square(i))
    
    end_time = time.time()-start_time
    
    print("Processing " + str(len(numbers)) + " numbers took " + str(end_time) + " time using serial processing.")

def sum_square_with_threads(numbers):
    start_time=time.time()
    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        result=list(executor.map(sum_square, numbers))
        print(result)

    end_time=time.time()-start_time
    print("Processing " + str(len(numbers)) + " numbers took " + str(end_time) + " time using threads from multiproccessing.")

if __name__== '__main__':

    numbers=range(10000) 
    sum_square_with_mp(numbers)
    sum_square_no_mp(numbers)
    sum_square_with_threads(numbers)

    
    

    