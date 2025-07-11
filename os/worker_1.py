# worker.py
import sys
import os
import time

def print_str(st):
    for i in range(20):
        print(st + " pid:" + str(os.getpid()) + "--> " +  str(i))
        time.sleep(2)
    print(st +  " finished with ", flush=True)

st = sys.argv[1]
print_str(st)
print("finsihed " + st)
