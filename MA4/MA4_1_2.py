
"""
Solutions to module 4
Review date:
"""

student = """Albin Svensson"""
reviewer = ""

import math as m
import random as r

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
    #Calculate the exact volume of the hypersphere
    return (m.pi ** (d/2)) / m.gamma((d/2) + 1) 
     
def main():
    n = 100000
    d = [2,11]
    
    for i in d:
        approx_volume = sphere_volume(n,d)
        exact_volume = hypersphere_exact(n,d)
        print(f"Approximated volume of the hypersphere with {i} dimensions: {approx_volume}")
        print(f"Exact volume of the hypersphere with {i} dimensions: {exact_volume}")


if __name__ == '__main__':
	main()
