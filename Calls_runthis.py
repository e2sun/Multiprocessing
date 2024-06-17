#bash stands for "born again shell"
from multiprocessing import Pool
import subprocess
import time



def run_bash(filenumber):
    #Calls the runthis shell script   
    cmd = "runthis.sh"
    to_bash=["bash",cmd, filenumber] 
    subprocess.call(to_bash)

def do_mp(filenumbers):
    

    p=Pool()
    p.map(run_bash, filenumbers)
    
    p.close()
    p.join()

    

    



def no_mp(filenumbers):
    for filenumber in filenumbers:
        run_bash(filenumber)
    




if __name__=='__main__':
    filenumbers=list(map(str,range(10)))

    start_time1=time.time()
    do_mp(filenumbers)
    end_time1 = time.time()-start_time1
   

    start_time2=time.time()
    no_mp(filenumbers)
    end_time2 = time.time()-start_time2

    print("Processing " + str(len(filenumbers)) + " files took " + str(end_time1) + " time using multiprocessing.")
    print("Processing " + str(len(filenumbers)) + " files took " + str(end_time2) + " time using serial processing.")