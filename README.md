# project_euler

Project Euler is a website dedicated to providing challenging mathematical problems intended to be solved with computer programming. This repository contains the code I have written to solve them (so far, Python only).


I will upload my solutions to Project Euler problems in sequential order. I will only upload a solution for a later problem (even if I have solved it) after I have first solved (i.e., have a correct solution that runs in under one-minute) and uploaded solutions for all prior problems.
Currently uploaded Problems 1-17.

I maintain a personal functions.py file containing reusable functions I've written for these problems. However, I do not upload that file here as it would be too difficult to continually update. Instead, for each problem.py solution, I copy only the specific functions needed into methods within the Solution class. Even if I reuse the same function for multiple solutions to a problem, I paste separate copies into each Solution class. If I later improve a function in my personal functions.py, I use the new version for future problems needing it; but I don't retroactively update past solutions using the old function. This both ensures that all Solution classes are wholly self-contained, and more authentically shows how I actually solved each problem, with the specific function implementation in each Solution class contained as they were actually written. In any case, that Solution (at least one of them!) runs in under a minute.
