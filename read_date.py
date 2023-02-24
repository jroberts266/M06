#M06 Programming Assignment
#Author: Joey Roberts
#Date: 2/23/2023
# Programming assigments to read a parse data from string a multiprocess


import time
import random
import multiprocessing
import os

# open and reads text file
file1 = open(r"C:\Users\joeyf\OneDrive\Ivy Tech\SDEV220\M06\today.txt","r")
today_string = file1.read()
# prints date string
print(today_string)
# parses date string
today = today_string.split('/')
#prints date string
print(today)

# creates function whoami
def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

# modified example from book to demonstrate mulitprocessing
if __name__ == "__main__":
    for n in range(3):
        wait = multiprocessing.Process(target=whoami, args=("I'm function %s" % n,)) 
        wait.start()
        delay = random.uniform(0, 1)
        time.sleep(delay)
        print(time.ctime())