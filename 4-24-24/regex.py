#!/usr/bin/env python3

import re

filename = input("Enter the filename to be searched: ")

txt = input("Enter the search expression: ")

print(f"Filename: {filename}")

found = 0

with open(filename) as f:
    for line in f:
        match = re.search(txt, line)
        if match:
            found = 1
            # print("Found: ", match.string) #disabling since the project said only to say if it was found or not
            break
if found == 0:
    print("Nothing found")
else:
    print("It was found!")
