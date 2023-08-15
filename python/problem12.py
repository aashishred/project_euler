import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)

from math import sqrt

# Highly Divisible Triangular Number
target = 500


class Solution1:
    # Takes about a minute and a half to run.

    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0
        self.numberOfDivisors = lambda x: len(self.factors(x))

    def factors(self, n):
        # Returns a sorted list of all the factors of n
        factorList = [1, n]
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                factorList.append(i)
                factorList.append(n // i)
        return sorted(list(set(factorList)))

    def solve(self):
        n = 1
        increment = 2
        while True:
            if self.numberOfDivisors(n) > target:
                self.answer = n
                break
            else:
                n += increment
                increment += 1
        return self.answer


class Solution2:
    # Takes just over ~30 seconds to run
    # Using the fact that the nth triangle number is given by:
    # T_n = 1/2 * n * (n+1)

    def __init__(self):
        self.answer = 0
        self.numberOfDivisors = lambda x: len(self.factors(x))

    def factors(self, n):
        # Returns a sorted list of all the factors of n
        factorList = [1, n]
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                factorList.append(i)
                factorList.append(n // i)
        return sorted(list(set(factorList)))

    def solve(self):
        n = 1
        while True:
            triangleNumber = n * (n + 1) * 0.5
            if self.numberOfDivisors(triangleNumber) > target:
                self.answer = int(triangleNumber)
                break
            else:
                n += 1
        return self.answer


class Solution3:
    # This is basically the solution I used last time; takes over three minutes to run.

    def __init__(self):
        self.answer = 0
        self.numberOfDivisors = lambda x: len(self.factors(x))

    def isTriangleNumber(self, n):
        # Returns True iff n is a triangle number, False otherwise
        return sqrt(8 * n + 1) % 1 == 0

    def factors(self, n):
        # Returns a sorted list of all the factors of n
        factorList = [1, n]
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                factorList.append(i)
                factorList.append(n // i)
        return sorted(list(set(factorList)))

    def solve(self):
        n = 1
        while True:
            if self.isTriangleNumber(n) and (self.numberOfDivisors(n) > target):
                self.answer = n
                break
            n += 1
        return self.answer


if __name__ == "__main__":
    tracemalloc.start()  # Start memory allocation trace
    start = time.time()  # Start timer

    solution = Solution2()  # Change Solution1 to Solution2 etc., to run a different solution
    answer = solution.solve()  # Runs the solution

    print("Total elapsed time:", time.time() - start)  # Prints total time taken to run the solve() method
    print("Memory Usage\tCurrent:", tracemalloc.get_traced_memory()[0], "\tPeak:", tracemalloc.get_traced_memory()[1])  # Prints the current and peak memory usage in bytes of the traced Python objects

    tracemalloc.stop()  # Stops the memory allocation trace

    print("\n", os.path.basename(__file__))  # Prints the name of the problem (file name)
    print("Answer:", answer)  # Prints the answer returned by the solution
    pyperclip.copy(answer)  # Copies the answer to clipboard (to be pasted directly into Project Euler).
