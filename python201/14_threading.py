"""
threads - small units of work
- usually contained in processes

a process can have more than one thread
- the threads share the memory and state of the process

threading - a way of telling your code to do more than thing at once
- can be useful to improve speed by perfomring actions concurrently
- for a program to remain responsive to input while also performing some
other action which may be blocking

each process has at least one thread known as the main

References
---------------
https://en.wikipedia.org/wiki/Thread_(computing)
https://en.wikipedia.org/wiki/Child_process
https://en.wikipedia.org/wiki/Concurrency_(computer_science)
"""

import threading, time
from datetime import datetime

def sleeper(i):
    print("Hello from %d" % i)
    time.sleep(i)
    print("Goodbye from %d" % i)

print(datetime.now().strftime("%H:%M:%S"))
# sleeper(0)
# sleeper(1)
# sleeper(2)
# sleeper(3)

# threading.Thread(target=sleeper, args=(0,)).start()
# threading.Thread(target=sleeper, args=(1,)).start()
# threading.Thread(target=sleeper, args=(2,)).start()
# threading.Thread(target=sleeper, args=(3,)).start()

# threading.Timer(0, sleeper, [0]).start()
# threading.Timer(1, sleeper, [1]).start()
# threading.Timer(2, sleeper, [2]).start()
# threading.Timer(3, sleeper, [3]).start()

print(datetime.now().strftime("%H:%M:%S"))

stop = False

# def input_thread():
#     global stop
#     while True:
#         user_input = input('Should we stop?: ')
#         print(f">> User says: {user_input}")
#         if user_input == "yes":
#             stop = True
#             break

# def output_thread():
#     global stop
#     count = 0
#     while not stop:
#         print(count)
#         count += 1
#         time.sleep(1)

# t1 = threading.Thread(target=input_thread).start()
# t2 = threading.Thread(target=output_thread).start()

# ----------locking threading ------
data_lock = threading.Lock()
data = [x for x in range(100)]

def sync_consume_thread():
    global data_lock, data
    while True:
        data_lock.acquire()
        if len(data) > 0:
            print(threading.current_thread().name, data.pop())
        data_lock.release()

threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()

