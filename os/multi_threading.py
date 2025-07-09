import threading
import time

# def print_numbers():
#     for i in range(5):
#         print(f"Thread: {i}")
#         time.sleep(10)


# # Create thread
# t = threading.Thread(target=print_numbers)

# t.start()  # Run thread
# # time.sleep(5)
# t.join()   # Wait for thread to finish





def download_file(name):
    # print(f">>>> Downloading {name}...\n")
    for i in range(4):
        # print(i,"for. \n ")
        pass
    time.sleep(3)
    for i in range(3):
    
        print(i,"for2222>>>>>>\n<<<<")

    # print(f"done {name} downloaded.\n")


t1 = threading.Thread(target=download_file, args=("file1",))
t2 = threading.Thread(target=download_file, args=("file2",))
# t3 = threading.Thread(target=download_file, args=("file3",))

t1.start()
t2.start()
# t3.start()

t1.join()
# # t2.join()
# t3.join()
