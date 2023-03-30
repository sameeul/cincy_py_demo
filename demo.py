import time
import numpy as np
import math

import libtest

def calc_sum_of_squares(n):
    in_array = np.ones((n), dtype=np.uint32)
    return np.sum(np.square(in_array))

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    for i in range(2, math.ceil(math.sqrt(n))):
        if n%i == 0:
            return False
    
    return True


def count_primes(n):
    count = 0
    for i in range(1,n+1):
        if is_prime(i):
            count +=1
    return count

def test_sum_of_elements(n):
    data = np.ones((n), dtype=np.uint16)
    #sum = libtest.sum_of_elements(data)
    sum = np.sum(data)
    return sum

if __name__ == "__main__":

    sample_size = 10

    for i in range(sample_size):
        start_time = time.time()
        #tmp = calc_sum_of_squares(100000000)
        #tmp = libtest.calc_sum_of_squares(100000000)


        count = libtest.count_primes(10000)
        #count = count_primes(10000)
        
        #out = test_sum_of_elements(100000000)
        #out = np.sum(np.ones((100000000), dtype=np.uint16))
        
        end_time = time.time()
        print(f"elapsed time = {1000*(end_time-start_time)} ms")

