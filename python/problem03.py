import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)

from math import sqrt, floor

# Largest Prime Factor
target = 600_851_475_143


class Solution1:
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0

    def factors(self, n):  # Returns a sorted list of all the factors of n
        factorList = [1, n]
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                factorList.append(i)
                factorList.append(n // i)
        return sorted(list(set(factorList)))

    def isPrime(self, n):  # Returns True iff n is prime, False otherwise.
        if n <= 1:
            return False
        elif n < 4:
            return True
        elif (n % 2 == 0):
            return False
        elif n < 9:
            return True
        elif (n % 3 == 0):
            return False
        else:
            r = floor(sqrt(n))
            f = 5
            while f <= r:
                if n % f == 0:
                    return False
                if n % (f + 2) == 0:
                    return False
                f += 6
        return True

    def primeFactors(self, n):  # Returns a sorted list of all the prime factors of n
        factorList = self.factors(n)
        primeFactorList = [x for x in factorList if self.isPrime(x)]
        return primeFactorList

    def solve(self):
        self.answer = self.primeFactors(target)[-1]
        return self.answer


if __name__ == "__main__":
    tracemalloc.start()  # Start memory allocation trace
    start = time.time()  # Start timer

    solution = Solution1()  # Change Solution1 to Solution2 etc., to run a different solution
    answer = solution.solve()  # Runs the solution

    print("Total elapsed time:", time.time() - start)  # Prints total time taken to run the solve() method
    print("Memory Usage\tCurrent:", tracemalloc.get_traced_memory()[0], "\tPeak:", tracemalloc.get_traced_memory()[1])  # Prints the current and peak memory usage in bytes of the traced Python objects

    tracemalloc.stop()  # Stops the memory allocation trace

    print("\n", os.path.basename(__file__))  # Prints the name of the problem (file name)
    print("Answer:", answer)  # Prints the answer returned by the solution
    pyperclip.copy(answer)  # Copies the answer to clipboard (to be pasted directly into Project Euler).
