import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)

# Longest Collatz Sequence
target = 1_000_000


class Solution1:
    # Takes about a minute and a half to run.

    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0
        self.count = 0
        self.longest = 0
        self.lengths = [len(self.iterativeCollatzChain(x)) for x in range(1, target)]

    def iterativeCollatzChain(self, n):
        chain = []
        while n != 1:
            chain.append(n)
            if n % 2 == 0:
                n //= 2
            else:
                n = (3 * n) + 1
        chain.append(1)
        return chain

    def solve(self):
        for length in self.lengths:
            self.count += 1
            if length > self.longest:
                self.longest = length
                self.answer = self.count
        return self.answer


class Solution2:
    # This was my old solution. Takes just over a minute to run!

    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0
        self.lengths = {}

    def solve(self):
        for n in range(1, target):
            num = n
            count = 1
            while n != 1:
                count += 1
                if n % 2 == 0:
                    n //= 2
                else:
                    n = (3 * n) + 1
            self.lengths[num] = count
        self.answer = max(self.lengths, key=self.lengths.get)
        return self.answer


class Solution3:
    # Runs in under 10 seconds

    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0
        self.memo = {1: 1}  # Initialise memo dictionary with base case
        self.lengths = (self.collatzLength(x) for x in range(1, target))  # Use generator expression

    def collatzLength(self, n):
        # Use memoization to avoid repeated calculations
        if n not in self.memo:
            if n % 2 == 0:
                self.memo[n] = 1 + self.collatzLength(n // 2)
            else:
                self.memo[n] = 2 + self.collatzLength((3 * n + 1) // 2)
        return self.memo[n]

    def solve(self):
        # Use max function with key argument to find the number with the longest chain
        self.answer = max(range(1, target), key=self.collatzLength)
        return self.answer


if __name__ == "__main__":
    tracemalloc.start()  # Start memory allocation trace
    start = time.time()  # Start timer

    solution = Solution3()  # Change Solution1 to Solution2 etc., to run a different solution
    answer = solution.solve()  # Runs the solution

    print("Total elapsed time:", time.time() - start)  # Prints total time taken to run the solve() method
    print("Memory Usage\tCurrent:", tracemalloc.get_traced_memory()[0], "\tPeak:", tracemalloc.get_traced_memory()[
        1])  # Prints the current and peak memory usage in bytes of the traced Python objects

    tracemalloc.stop()  # Stops the memory allocation trace

    print("\n", os.path.basename(__file__))  # Prints the name of the problem (file name)
    print("Answer:", answer)  # Prints the answer returned by the solution
    pyperclip.copy(answer)  # Copies the answer to clipboard (to be pasted directly into Project Euler).
