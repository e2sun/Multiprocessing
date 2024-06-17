#MultiProcessing Tutorial
#https://www.youtube.com/watch?v=RR4SoktDQAw&t=290s 

#Video1: Introduction (Part 1)
#Introducing a simple example of multiprocessing module in Python
#We show how to simply apply this module to a function that takes a number and squares it

import os
from multiprocessing import Process, current_process

def square(number):
    result=number*number


#We can use the "os" module in Python to print out the Process ID
#assigned to the call of this function assigned by the operating system

    process_id=os.getpid()
    print("Process ID: " + str(process_id))

    print("The number " + str(number) + " squares to " + str(result))

if __name__=='__main__':
    processes=[]
    numbers=[1,2,3,4]
    
    for number in numbers:
        process=Process(target=square, args=(number,))
        processes.append(process)

        #Processes are spwaned by creating a Process object
        #then calling its start() method

        process.start();
    
    
