import time, tracemalloc  # Used for efficiency tracking of elapsed time and memory usage
import pyperclip  # Used to automatically copy the answer to clipboard
import os  # Used to print the name of the problem (i.e., file name)

# Number Letter Counts
target = 1000


class Solution1:
    # Quite ugly, with some obvious retrofitting to things that didn't work. But runs quickly and correctly.

    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0
        self.numberLetter = {
            0: "",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            100: "onehundred",
            1000: "onethousand"
        }

    def solve(self):
        for i in range(target + 1):
            count = 0
            if i in self.numberLetter:
                count += len(self.numberLetter[i])
            else:
                number = str(i)
                if len(number) == 2:  # 2-digit numbers. NB: We have already considered numbers from 1-20.
                    count += len(self.numberLetter[10 * int(number[0])])  # Number in the 10s place, e.g., thirty
                    count += len(self.numberLetter[int(number[1])])  # Number in the units place, e.g., six
                if len(number) == 3:  # 3-digit numbers
                    count += len(self.numberLetter[int(number[0])])  # Number in the hundreds place, e.g., eight
                    count += len("hundred")
                    if (i % 100) != 0:  # i.e., so long as the number isn't an even "seven hundred", etc.
                        count += 3  # "and"
                        if int(number[1] + number[2]) in self.numberLetter:  # To deal with numbers which are something hundred and something-teen; as they are not four hundred and ten three.
                            count += len(self.numberLetter[int(number[1] + number[2])])
                        else:
                            count += len(self.numberLetter[10 * int(number[1])])  # Number in the 10s place, e.g., forty
                            count += len(self.numberLetter[int(number[2])])  # Number in the units place, e.g., six
            self.answer += count
        return self.answer


class Solution2:
    # The solution I used last time:
    
    def __init__(self):
        self.answer = 0  # Initialise answer variable to 0
        self.letters = {
        0: len(""),
        1: len("one"),
        2: len("two"),
        3: len("three"),
        4: len("four"),
        5: len("five"),
        6: len("six"),
        7: len("seven"),
        8: len("eight"),
        9: len("nine"),
        10: len("ten"),
        11: len("eleven"),
        12: len("twelve"),
        13: len("thirteen"),
        14: len("fourteen"),
        15: len("fifteen"),
        16: len("sixteen"),
        17: len("seventeen"),
        18: len("eighteen"),
        19: len("nineteen"),
        20: len("twenty"),
        30: len("thirty"),
        40: len("forty"),
        50: len("fifty"),
        60: len("sixty"),
        70: len("seventy"),
        80: len("eighty"),
        90: len("ninety"),
        100: len("onehundred"),
        1000: len("onethousand")
    }

    def count(self, n):
        # Accounts for all numbers <= 20
        # Accounts for all multiples of 10
        if n in self.letters:
            return self.letters[n]

        # Accounts for all multiples of 100
        elif (n % 100 == 0) and (n != 100):
            return self.letters[n // 100] + len("hundred")

        elif 20 < n < 100:
            return self.letters[10 * (n // 10)] + self.letters[int(str(n)[1])]

        elif 100 < n < 1000:
            return self.count(100 * (n // 100)) + len("and") + self.count(n - (100 * (n // 100)))

    def solve(self):
        self.answer = sum(self.count(x) for x in range(1001))
        return self.answer


if __name__ == "__main__":
    tracemalloc.start()  # Start memory allocation trace
    start = time.time()  # Start timer

    solution = Solution2()  # Change Solution1 to Solution2 etc., to run a different solution
    answer = solution.solve()  # Runs the solution

    print("Total elapsed time:", time.time() - start)  # Prints total time taken to run the solve() method
    print("Memory Usage\tCurrent:", tracemalloc.get_traced_memory()[0], "\tPeak:", tracemalloc.get_traced_memory()[
        1])  # Prints the current and peak memory usage in bytes of the traced Python objects

    tracemalloc.stop()  # Stops the memory allocation trace

    print("\n", os.path.basename(__file__))  # Prints the name of the problem (file name)
    print("Answer:", answer)  # Prints the answer returned by the solution
    pyperclip.copy(answer)  # Copies the answer to clipboard (to be pasted directly into Project Euler).
