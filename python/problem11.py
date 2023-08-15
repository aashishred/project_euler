import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)


# Largest Product in a Grid

class Solution1:
    # Pretty much exactly how I solved it before. TODO: find a new solution.
    
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0
        self.grid = [[int(t) for t in s.split(" ")] for s in open("problem11.txt", "r").read().split("\n") if s]  # problem11.txt is just a file containing the grid copy & pasted.

    def solve(self):
        horizontal = max(self.grid[i][j] * self.grid[i][j+1] * self.grid[i][j+2] * self.grid[i][j+3] for i in range(20) for j in range(17))
        vertical = max(self.grid[i][j] * self.grid[i+1][j] * self.grid[i+2][j] * self.grid[i+3][j] for i in range(17) for j in range(20))
        rightDiagonal = max(self.grid[i][j] * self.grid[i+1][j+1] * self.grid[i+2][j+2] * self.grid[i+3][j+3] for i in range(17) for j in range(17))
        leftDiagonal = max(self.grid[i][j] * self.grid[i-1][j+1] * self.grid[i-2][j+2] * self.grid[i-3][j+3] for i in range(3, 20) for j in range(17))
        
        self.answer = max(horizontal, vertical, rightDiagonal, leftDiagonal)
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
