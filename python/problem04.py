import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
import pyperclip
import os

# Largest Palindrome Product


class Solution1:
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0

    def reverse(self, S):  # Whatever the type of n, returns a STRING which is n backwards.
        return str(S)[::-1]

    def isPalindrome(self, n): # Returns true iff n is a palindrome, False otherwise.
        x = str(n)
        if x[-1] == '0':
            return False
        elif self.reverse(x) == x:
            return True

    def solve(self):
        palindromes = []
        for i in reversed(range(100, 1000)):
            for j in reversed(range(100, 1000)):
                product = i*j
                if self.isPalindrome(product):
                    palindromes.append(product)
        self.answer = max(palindromes)
        return self.answer


class Solution2:
    def __init__(self):
        self.answer = 0

    def reverse(self, S):  # Whatever the type of n, returns a STRING which is n backwards.
        return str(S)[::-1]

    def isPalindrome(self, n): # Returns true iff n is a palindrome, False otherwise.
        x = str(n)
        if x[-1] == '0':
            return False
        elif self.reverse(x) == x:
            return True

    def solve(self):
        largestPalindrome = 0
        for i in reversed(range(100, 1000)):
            if (i % 11) == 0:
                j = 999
                k = 1
            else:
                j = 990
                k = 11
            while j >= i:
                product = i*j
                if product <= largestPalindrome:
                    break
                if self.isPalindrome(product):
                    largestPalindrome = product
                j -= k
            i -= 1
        self.answer = largestPalindrome
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
