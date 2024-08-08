#bash stands for "born again shell"
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, as_completed, wait
from multiprocessing import Pool
import multiprocessing as mp
from multiprocessing.pool import ThreadPool
import os
import subprocess
import time



def run_bash(filenumber):
    #Calls the runthis shell script   
    cmd = "runthis.sh"
    to_bash=["bash",cmd, filenumber] 
    subprocess.call(to_bash)


# def LetMeTry(filenumbers):
#     max_workers = 2 * os.cpu_count()  # Example: Adjust based on your system capabilities
#     with ThreadPoolExecutor(max_workers=max_workers) as executor:
#         executor.map(run_bash, filenumbers)



def do_mp_with_Pool(filenumbers):
    

    p=Pool(processes=mp.cpu_count())
    p.map_async(run_bash, filenumbers)
    
    p.close()
    p.join()

def do_mp_with_Pool_chunksize(filenumbers):
    

    p=Pool(processes=mp.cpu_count())
    p.map_async(run_bash, filenumbers, chunksize=2)
    
    p.close()
    p.join()

def do_mt_with_Thread_Pool_Executor(filenumbers):
    with ThreadPoolExecutor() as executor:
        executor.map(run_bash, filenumbers)
        

def no_mp(filenumbers):
    for filenumber in filenumbers:
        run_bash(filenumber)
    

if __name__=='__main__':

    filenumbers=list(map(str,range(30000)))

    start_time1=time.time()
    do_mp_with_Pool(filenumbers)
    end_time1 = time.time()-start_time1

    # start_time2=time.time()
    # do_mp_with_Pool_chunksize(filenumbers)
    # end_time2 = time.time()-start_time2

    start_time3=time.time()
    do_mt_with_Thread_Pool_Executor(filenumbers)
    end_time3 = time.time()-start_time3
    
    #start_time4=time.time()
    #no_mp(filenumbers)
    #end_time4 = time.time()-start_time4

    #print("Processing " + str(len(filenumbers)) + " files took " + str(end_time0) + " seconds using Let me Try method")
    print("Processing " + str(len(filenumbers)) + " files took " + str(end_time1) + " seconds using Pool in multiprocessing.")
    #print("Processing " + str(len(filenumbers)) + " files took " + str(end_time2) + " seconds using Pool with chunksize in multiprocessing.")
    print("Processing " + str(len(filenumbers)) + " files took " + str(end_time3) + " seconds using Thread Pool Executor.")
    #print("Processing " + str(len(filenumbers)) + " files took " + str(end_time4) + " seconds using serial processing.")
   
    


    
   
   


    

    