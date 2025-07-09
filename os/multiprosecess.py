from multiprocessing import Process

def compute():
    print("Running in new process")

p = Process(target=compute)
p.start()

p.join()
