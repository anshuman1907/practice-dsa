from threading import Thread, current_thread
import time


def print_str(st):
    for i in range(5):
        time.sleep(2)
        print(st + "--> " +  str(i))
    print(st +  " finished", flush=True)


if False:
    # crearting objects
    dasdasd = []
    for i in range(3):
        t = Thread(target=print_str, args=("thread " + str(i),))
        dasdasd.append(t)

    # start procesing
    for i in dasdasd:
        i.start()

    # finish processing.
    for j in dasdasd:
        j.join()

    print("-finished.")

    print(f"Final threads: {len(dasdasd)}")
    #  100_000


if True:
    # crearting objects
    t1 = Thread(target=print_str, name="thread 1", args=("thread 1",), daemon=True)
    t2 = Thread(target=print_str, name="thread 2", args=("thread 2",), daemon=True)
    t3 = Thread(target=print_str, name="thread 3", args=("thread 3",), daemon=True)
    main_thread = current_thread()

    # start procesing
    t1.start()
    t2.start()
    t3.start()

    # finsih processing
    t1.join()
    t2.join()
    t3.join()

    print("-finished.")
