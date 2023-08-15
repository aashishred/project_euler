import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)

# Special Pythagorean Triplet
target = 1000


class Solution1:
    # Using the fact that we can generate Pythagorean triplets, using:
    # a = m^2 - n^2; b = 2mn; c = m^2 + n^2
    # Where m and n are positive integers, with m > n

    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0

    def solve(self):
        for m in range(1, target):
            for n in range(1, m):
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                total = a + b + c

                if total == target:
                    self.answer = a * b * c
                    break
        return self.answer


class Solution2:
    # Just to see how long a brute force would take!

    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0

    def solve(self):
        for a in range(1, target):
            for b in range(1, target):
                for c in range(1, target):
                    if (a * a) + (b * b) == (c * c):
                        if a + b + c == target:
                            self.answer = a * b * c
                            break
        return self.answer


class Solution3:
    # The solution I used last time; quicker than solution1 (which is annoying, as this is so primitive).

    def __init__(self):
        self.answer = 0

    def solve(self):
        for a in range(1, target):
            for b in range(1, a):
                c = (a ** 2 + b ** 2) ** 0.5
                if c % 1 == 0:
                    if a + b + c == target:
                        self.answer = int(a * b * c)
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
