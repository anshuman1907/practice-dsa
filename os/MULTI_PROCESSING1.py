from multiprocessing import Process
import time

def print_str(st):
    for i in range(5):
        time.sleep(2)
        print(st + "--> " +  str(i))
    print(st +  " finished", flush=True)

if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]
    processes = []

    for i in numbers:
        p = Process(target=print_str, args=("thread " + str(i),))
        processes.append(p)
    
    # start procesing
    for i in processes:
        i.start()

    # wait for processing
    for p in processes:
        p.join()

    print("All processes finished.")
