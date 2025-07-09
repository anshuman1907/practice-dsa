from multiprocessing import Process



# def compute():
#     print("Running in new process")

# p = Process(target=compute)
# p.start()

# p.join()



from multiprocessing import Pool
import os
import time
def square(n):
    
    return n * n
time.sleep(3)

if __name__ == "__main__":
    with Pool(processes=os.cpu_count()) as p:
        
        result = p.map(square, [1, 2, 3, 4, 5])
        
        print("✅ Squares:", result)
