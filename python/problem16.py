import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)

# Power Digit Sum
target = 2**1000


class Solution1:
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0

    def digitSum(self, n):
        return sum(int(x) for x in str(n))

    def solve(self):
        self.answer = self.digitSum(target)
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
