#!/usr/bin/env python3

import os

filename = "myfile.txt"

print("You are about to remove the file: ", filename)
answer = input("Are you sure you want to do this? y/n: ")

if answer == "y":
    os.remove(filename)
    print("File deleted")
else:
    print("Ok, I did not delete the file")
