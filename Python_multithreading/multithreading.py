## Multithreading

## when to use Multi Threading.

##I/O- bound tasks: Tasks that spend more time waiting for I/O operation.(e.g - file operation).
### Concurrent execution : When you want to improve the thoughput of your application.


import threading
import time

def print_no():
    for i in range(5):
        time.sleep(2)
        print(f"Number{i}")

def print_letter():
    for l in "abcde":
        time.sleep(2)
        print(f"Letter{l}")


## Create a two thread
t1= threading.Thread(target=print_no)
t2 = threading.Thread(target=print_letter)

t= time.time()
print(t)
t1.start()
t2.start()
finished_time = time.time()-t
t1.join()
t2.join()
print(finished_time)