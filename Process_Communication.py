#MultiProcessing Tutorial
#https://www.youtube.com/watch?v=TQx3IfCVvQ0&list=PL5tcWHG-UPH3SX16DI6EP1FlEibgxkg_6&index=6

#Video 6: Process Communication
#We show how to make use of the multiprocessing Queue
#Class to communicate between different processes

from multiprocessing import Process, Queue

#Loop through the list of numbers given and place the squares into the queue
def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)


def cube(numbers, queue):
    for i in numbers:
        queue.put(i*i*i)


if __name__=='__main__':
    
    numbers = range(5) 
    queue=Queue()

    square_process=Process(target=square, args=(numbers, queue))
    cube_process=Process(target=cube, args=(numbers, queue))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print(queue.get())

