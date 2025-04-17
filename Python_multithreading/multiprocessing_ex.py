## Process that run in parallel
### CPU- Bound tasks- Tasks that are heavy on CPU usage(heavy mathematical computations)
## paraller execution - Multiple core of the CPU.

import multiprocessing

import time

def square_no():
    for i in range(5):
        time.sleep(1)
        print(i*i)

def cube_no():
    for i in range(5):
        time.sleep(1.5)
        print(i*i*1)

if __name__=="__main__":

    p1 = multiprocessing.Process(target=square_no)
    p2 = multiprocessing.Process(target=cube_no)

    ## start the process

    t = time.time()


    p1.start()
    p2.start()




    ## wait

    p1.join()
    p2.join()

    print(time.time()-t)