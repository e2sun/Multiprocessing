#This class creates multiple text files in python

import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-n', type=str, required=True, help="This is a helpful comment.")

    return parser.parse_args()
    

def createTextFile(number):
    subprocess.call('mkdir -p files', shell=True)
    
    f=open(f'files/file{number}.txt','w') 
    


if __name__ == '__main__':
    print("Running code...")
    args=parse_args()
    filenumber=args.n
    createTextFile(filenumber)
#for i in range(5):
    #f = open(f'file{i}.txt','w') 
   


