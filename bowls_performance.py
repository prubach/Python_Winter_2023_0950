from time import time
from bowls_count import *

def time_func(func, n):
    t0 = time()
    print('Calling: {} for n={}'.format(func, n))
    print('Result sum={}'.format(func(n)))
    t1 = time()
    elapsed = t1 - t0
    print(f'It took: {elapsed} sec')

n = 200000000
time_func(bowls_loop_1, n)
time_func(bowls_loop_2, n)
#time_func(bowls_recursive, n)
time_func(bowls_sequence, n)