
"""
Solutions to module 4
Review date:
"""

student = """Albin Svensson"""
reviewer = ""

import math as m
import random as r

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
