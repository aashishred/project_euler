import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)

# Smallest Multiple
target = 20


class Solution1:
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0

    def solve(self):
        number = 2520
        while True:
            count = 10
            for i in range(11, target+1):
                if number % i == 0:
                    count += 1
            if count == target:
                self.answer = number
                break
            else:
                number += 2520
        return self.answer


class Solution2:  # The solution I used last time
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0

    def solve(self):
        n = 2520
        found = False

        while not found:
            count = 0
            for i in range(11, 20):
                if n % i == 0:
                    count += 1
            if count != 9:
                n += 2520
            else:
                self.answer = n
                break
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
