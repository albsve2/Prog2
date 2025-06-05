"""
Solutions to module 1
Student: Albin Svensson
Mail: albin.svensson.7131@student.uu.se
Reviewed by:
Reviewed date:
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""


import time
import math

def multiply(m: int, n: int) -> int:
    """ Computes m*n using additions"""
    if m > n :
        if n == 0:
            return 0
        else:
            return m + multiply(m, n-1)
    else:
        if m == 0:
            return 0
        else:
            return n + multiply(n, m-1)


def harmonic(n: int) -> float:
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


def get_binary(x: int) -> str:
    """ Returns the binary representation of x """
    if x == 0:
        return '0'
    elif x == 1:
        return '1'
    elif x < 0:
        return '-' + get_binary(-x)
    else:
        return get_binary(x//2) + str(x%2)


def reverse_string(s: str) -> str:
    """ Returns the s reversed """
    return s if len(s) <= 1 else reverse_string(s[1:]) + s[0]


def largest(a: iter):
    """ Returns the largest element in a"""
    if len(a) == 1:
        return a[0]
    else:
        max_of_rest = largest(a[1:])
        return a[0] if a[0] > max_of_rest else max_of_rest


def count(x, s: list) -> int:
    """ Counts the number of occurrences of x on all levels in s"""
    if not s: #check if s is empty
        return 0
    if x == s: #check if x is equal to s
        return 1
    count_first = count(x, s[0]) if isinstance(s[0], list) else (s[0] == x) #check if x is a list or the first element in s is equal to x
    count_res = count(x, s[1:]) #count the rest of the list
    return count_first + count_res #return the total count


def bricklek(f: str, t: str, h: str, n: int) -> str:
    """ Returns a string of instruction to move the tiles """
    if n == 0:
        return []
    if n == 1:
        return [(f + '->' + t)]
    return bricklek(f, h, t, n-1) + [(f + '->' + t)] + bricklek(h, t, f, n-1)


def fib(n: int) -> int:
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    print('\nCode that demonstates my implementations\n')

    print('\n\nCode for analysing fib and fib_mem\n')

    #code to see that fibanocci grows as 1.618**n
    real_time = []
    n_values = range(32, 39)
    for n in n_values:
        start_time = time.perf_counter()
        fib(n)
        end_time = time.perf_counter()
        real_time.append(end_time - start_time)

    approx = [real_time[i]/real_time[i-1] for i in range(1,len(real_time))]
    print(f'Values close to 1.618: {approx}')
    print('Therefore we see that fibanocci grows as Theta(1.618**n)')
    def time_fib(n):
        #count the time for fib(39) 
        tstart = time.perf_counter()
        fib(39)
        tstop = time.perf_counter()
        C = (tstop-tstart) / (1.618**39) #value for constant C
        return C * (1.618**n) #calculate the estimate time for n = int

    print(f'Time for n = 50: {round(time_fib(50)/60, 2)} Minutes') #print time for n=50 in minutes
    print(f'Time for n = 100: {round(time_fib(100)/(3600*24*365*1000), 2)} thousand years') #print time for n=100 in thousand years
    # Print the 100th Fibonacci number
    tstart = time.perf_counter()
    print(f'Value for n = 100: {round(_fib(100), None)} and it took {time.perf_counter()-tstart} seconds')
    print('\nBye!')

def _fib(n):
    memory = {0: 0, 1: 1}
    def fib_mem(n):
        if n not in memory:
            memory[n] = fib_mem(n-1) + fib_mem(n-2)
        return memory[n]
    return fib_mem(n)

if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  
  t(n) = 2**n-1
  t(50) = 2**50-1 = 1125899906842623s = 35,7 million years
  
  
  Exercise 9: Time for Fibonacci:

    List on values close to 1.618: [1.6091066213826997, 1.6170549307209625, 1.6133170895152877, 1.6466333066083456, 1.621323010081735, 1.6219219051076006]
    Therefore we see that fibanocci grows as Theta(1.618**n)
    Time for n = 50: 66 Minutes
    Time for n = 100: 3,6 million years
    
  

  Exercise 10: Time for fib_mem:
  
    Value for n = 100: 354224848179261915075 and it took 0.000114000000000000
  
  Exercise 11: Comparison sorting methods:
  
    1000 elements takes 1 second

    Theta(n^2)
    Insertion sort whould take 10^6 seconds = 11.5 days for 10^6 elements and 10^12 seconds = 31,7 thousand years for 10^9 elements

    Theta(n log n)
    10^3 * log(10^3) * C = 1 => C = 1/(10^3 * log(10^3)) = 1/3000
    Merge sort whould take 10^6 * log(10^6) * (1/3000) = 33,3 minutes for 10^6 elements and 10^9 * log(10^9) * (1/3000) = 34,7 days for 10^9 elements
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  
    A takes N seconds for n elements
    B takes c*n*log(n) seconds for n elements
    B(10) = 1 second

    C = 1/(10*log(10)) = 0.1
    A(n) = n

    So n > 0.1*n*log(n)
    and solving this we get that when n > 10^10 is A faster than B
"""
