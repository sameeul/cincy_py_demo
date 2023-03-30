import time
import numpy as np
import math

import libtest

def calc_sum_of_squares(n):
    in_array = np.ones((n), dtype=np.uint32)
    sum = 0
    # for i in in_array:
    #     sum += i*i
    
    # return sum
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
    sum = libtest.sum_of_elements(data)
    print(sum)
    return sum

if __name__ == "__main__":
    start_time = time.time()
    #print(calc_sum_of_squares(100000000))

    #count = libtest.count_primes_v_lib(10000)
    #count = count_primes(10000)
    out = test_sum_of_elements(100000000)
    #out = np.sum(np.ones((100000000), dtype=np.uint16))
    end_time = time.time()
    print(f"{out} ")
    print(f"elapsed time = {1000*(end_time-start_time)} ms")

