#MultiProcessing Tutorial
#https://www.youtube.com/watch?v=itbx_hDX7z8 

#Video 2: Introduction (Part 2)
#Continuing on wih our introduction into the multiprocessing module 

import os
import time

from multiprocessing import Process, current_process

def square(numbers):
    for number in numbers:
        time.sleep(0.5)
        result=number*number
        print("The number " + str(number) + " squares to " + str(result))


if __name__=='__main__':

    #The processes list will store each call we make to "square"
    # and the numbers list contains the numbers we loop through and call the 
    #"square" function on.

    processes=[]
    #numbers=[1,2,3,4]
    numbers=range(100)

    #Loop through the list of numbers, call the "square" function
    for i in range(50):
        process=Process(target=square, args=(numbers,)) #Feed it the function and the argument
        processes.append(process)

        #Processes are spwaned by creating a Process object and then calling its start() method.
        process.start()

    for process in processes:
        process.join()
        
print("Multiprocessing complete")

        