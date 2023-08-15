import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)


# Large Sum
target = 10


class Solution1:
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0
        self.numbers = open("problem13.txt", "r").read().splitlines() # problem13.txt is a copy & paste of all the numbers on different lines, as shown in the problems

    def solve(self):
        digits = sum(int(x) for x in self.numbers)
        self.answer = str(digits)[:target]
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
