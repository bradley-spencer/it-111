#!/usr/bin/env python3

filename = "myfile.txt"

f = open(filename, "w")
f.write("Hello, this is my file, no one else's :)\n")
f.close()
