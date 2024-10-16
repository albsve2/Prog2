
"""
Solutions to module 4
Review date:
"""

student = """Albin Svensson"""
reviewer = ""


import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    inside = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for i in range(n):
        x = r.uniform(-1,1)
        y = r.uniform(-1,1)
        if x**2 + y**2 <= 1:
            inside += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    
    pi_approx = 4 * inside / n
    
    print(f"Number of dots inside the cirkel: {inside}")
    print(f"Approximation of π: {pi_approx}")

    plt.figure(figsize=(5,5))
    plt.scatter(x_inside, y_inside, color='red', s=1)
    plt.scatter(x_outside, y_outside, color='blue', s=1)
    plt.title(f'Approximation of pi with n = {n}')
    plt.savefig(f'pi_approximation_{n}.png')
    plt.show()

    return pi_approx

def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
