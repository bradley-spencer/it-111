#!/usr/bin/env python3

import os

infile = "Project2Input.txt"
outfile = "Project2Update.txt"

fin = open(infile, "a")

appending = input("Enter the text to append to the file (1 line):\n")
fin.write(appending)
fin.close()

print("Saving to", outfile)
fin = open(infile, "r")
fout = open(outfile, "w")
fout.write(fin.read())
fin.close()
fout.close()

os.remove(infile)
