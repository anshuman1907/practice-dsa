
import threading
import multiprocessing



def greet():
    print("hello anshu")


s= multiprocessing.Process(target=greet)
s.start()

s.join()


# 



def greet():
    print("hello anshu")


s=threading.Thread(target=greet)


s.start()

s.join()

