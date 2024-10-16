
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
import time
import concurrent.futures
def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    points = [[r.uniform(-1,1) for i in range(d)] for i in range(n)] #List comprehension
    
    #Chekc if points are inside the sphere, filter out the points that are not
    points_inside = filter(lambda point: sum(map(lambda x: x**2, point)) <= 1, points)
    
    #Count the number of points inside the sphere
    points_inside_count = len(list(points_inside))

    #Calculate the volume of the sphere
    volume = (2**d) * (points_inside_count / n)
    return volume

def hypersphere_exact(n,d):
    return (m.pi ** (d/2)) / m.gamma((d/2) + 1) 

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function 
     with concurrent.futures.ProcessPoolExecutor(max_workers=np) as executor:
        futures = [executor.submit(sphere_volume, n, d) for i in range(np)] 
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
     return sum(results) / np

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
     return 

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11

    for y in range (10):
        sphere_volume(n,d)


if __name__ == '__main__':
	main()
