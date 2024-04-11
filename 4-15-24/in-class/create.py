#!/usr/bin/env python3

filename = "myfile.txt"

try:
    f = open(filename, "x")
    f.close()
except:
    print("Error creating file:", filename)
