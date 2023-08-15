import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)


from math import sqrt, floor

# 1000st Prime
target = 10_001


class Solution1:
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0

    def isPrime(self, n): 
        # Returns True iff n is prime, False otherwise.

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
                if n % (f+2) == 0:
                    return False
                f  += 6
        return True

    def solve(self):
        count = 1
        number = 3
        while count < target:
            if self.isPrime(number):
                count += 1
            number += 2
        self.answer = number - 2
        return self.answer


class Solution2:
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0
        self.primes = [2]

    def isPrime(self, n): 
        # Returns True iff n is prime, False otherwise.

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
                if n % (f+2) == 0:
                    return False
                f  += 6
        return True

    def solve(self):
        n = 3
        while len(self.primes) < target:
            if self.isPrime(n):
                self.primes.append(n)
            n += 2
            
        self.answer = self.primes[-1]
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
