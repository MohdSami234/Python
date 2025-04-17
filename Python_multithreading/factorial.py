'''

real- World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculation, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distributed the workload across multiple
CPU cores, improving performance.


'''

import multiprocessing

import math
import sys
import time



# Increasing the maximum number of digits for integer covnersion

sys.set_int_max_str_digits(100000)


## Function to compute factorials of a given number


def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)

    print(f"Factorial of {number} is {result}")

    return result



if __name__ == "__main__":
    number = [5000,600,4040]
    start_time = time.time()


    ## Create a pool of worker process
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,number)

    end_time = time.time()

    print(f"result:{results}")
    print(f"time taken {end_time-start_time}")