#bash stands for "born again shell"


import subprocess

#Calls the runthis shell script   
cmd = "sbatch runthis.sh"

filenumber = "5"

to_bash=["bash",cmd, filenumber] 
subprocess.call(to_bash)
