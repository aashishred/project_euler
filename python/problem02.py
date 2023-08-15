import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)

from functools import lru_cache

# Even Fibonacci Numbers
target = 4_000_000


class Solution1:
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0

    def solve(self):
        x = 1
        y = 1
        while (x <= target) or (y <= target):
            if x <= target:
                if (x % 2 == 0):
                    self.answer += x
                x += y
            if y <= target:
                if (y % 2 == 0):
                    self.answer += y
                y += x
        return self.answer


class Solution2:
    def __init__(self):
        self.answer = 0

    @lru_cache
    def fib(self, n):  # Prints the nth Fibonacci number
        if n in [1, 2]:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def solve(self):
        n = 1
        while self.fib(n) < target:
            if self.fib(n) % 2 == 0:
                self.answer += self.fib(n)
            n += 1
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
