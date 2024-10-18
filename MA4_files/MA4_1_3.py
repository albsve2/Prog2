
"""
Solutions to module 4
Review date:
"""

student = """Albin Svensson"""
reviewer = ""

import math as m
import random as r
import concurrent.futures as future
from time import perf_counter as pc
def sphere_volume(n, d):
    # n is the number of points to generate
    # d is the number of dimensions of the sphere 
    inside = 0 #Counter for points inside the sphere
    radius = 1 
    for i in range(n):
        points = [r.uniform(-radius, radius) for i in range(d)]
        if sum(coord**2 for coord in points) <= radius**2:
            inside += 1
        
    volume = (2**d) * (inside / n)
    return volume

def hypersphere_exact(n,d):
    return (m.pi ** (d/2)) / m.gamma((d/2) + 1) 

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function 
    with future.ProcessPoolExecutor() as ex:
       results = ex.map(sphere_volume, [n]*np, [d]*np)
    return sum(results) / np

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    n_per_process = n // np #Making sure each process gets a fraction in this case a tenth
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, [n_per_process]*np, [d]*np)
    return sum(results) / np

def main():
    n_seq = 100000 #samples
    n_par = 1000000 #samples
    d = 11 #dimensions
    np = 10 #processes

    # part 1 -- parallelization of a for loop among 10 processes 
    time_start = pc() #10 times seq with 100,000 samples
    for i in range (10):
        sphere_volume(n_seq,d)
    time_stop = pc()
    print(f'Time of execution for sequential code: {time_stop - time_start} seconds') 

    time_start_parallel1 = pc() #10 times parallel with 1,000,000 samples
    sphere_volume_parallel1(n_par, d, np)
    time_stop_parallel1 = pc()
    print(f'Time of execution for parallel code 1: {time_stop_parallel1 - time_start_parallel1} seconds')

    # part 2 -- parallelization of the actual computations by splitting the data
    time_start_seq = pc() #One seq with 100,000 samples
    sphere_volume(n_seq, d)
    time_stop_seq = pc()
    print(f'Time of execution for sequential code: {time_stop_seq - time_start_seq} seconds')

    time_start_parallel2 = pc() #One parallel with 1,000,000 samples
    sphere_volume_parallel2(n_par, d, np)
    time_stop_parallel2 = pc()
    print(f'Time of execution for parallel code 2: {time_stop_parallel2 - time_start_parallel2} seconds')

if __name__ == '__main__':
	main()
