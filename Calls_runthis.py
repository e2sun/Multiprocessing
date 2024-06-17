#bash stands for "born again shell"
from multiprocessing import Pool
import subprocess



def run_bash(filenumber):
    #Calls the runthis shell script   
    cmd = "runthis.sh"
    to_bash=["bash",cmd, filenumber] 
    subprocess.call(to_bash)

def do_mp(filenumbers):
    p=Pool()
    result=p.map(run_bash, filenumbers)


    p.close()
    p.join()





if __name__=='__main__':
    filenumbers=list(map(str,range(5)))

    do_mp(filenumbers)