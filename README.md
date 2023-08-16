# project_euler

Project Euler is a website with a series of problems intended to be solved by computation.

Repository contains my solutions. I will only upload solutions when I have a working (sub 1-minute) solution for all prior problems in that particular programming language. Currently uploaded Problems 1-17 (so far, only in Python).

I will only upload the solution if I have an implementation which runs in one minute or less, but I will include prior, less efficient implementations in the file. In these cases, or for cases in which the solution takes more than a few seconds to run, comments indicate how long the program takes to arrive at a solution.

Note on recurring functions: I do have a functions.py file containing frequently used functions, but it is not uploaded here (too unwieldy to update it each time). Rather, for each problem.py file, I paste the functions I need from the functions.py file as methods in the Solution class. If I need the same function for more than one solution to the same problem, I will still copy and paste it as a method in each Solution class. In this way, each Solution is entirely self-contained within that class. If I find a more efficient way to write some function, I change it in the functions.py file and use the new version for any new problems that require it. But I don't go back and change the implementation in prior solutions. This is because it more authentically shows how I solved those problems; and because the old version (at least one of them) was efficient enough to run the code in less than a minute, as is.
