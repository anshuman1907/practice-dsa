import subprocess
import sys
import os


def print_str(st):
    for i in range(5):
        time.sleep(2)
        print(st + "--> " +  str(i))
    print(st +  " finished", flush=True)


if True:
    # creating subprocesses
    processes = []
    print("trigerrimnng from " + str(os.getpid()))
    for i in range(3):
        st = f"process {i}"
        p = subprocess.Popen(["python", "/Users/somansh/Documents/practice-dsa/os/worker_1.py", st])

        # p = subprocess.Popen([sys.executable, os.path.join(os.path.dirname(__file__), "worker.py"), st])
        processes.append(p)

    # wait for all to finish
    for p in processes:
        p.wait()

    print("-finished.")
    print(f"Final processes: {len(processes)}")
