import os
import sys
import shutil

number = sys.argv[1]

try:
    int(number)
except:
    print("Please enter a number.")
    exit()

os.mkdir(f"Day{number}")
f = open(f"Day{number}/day{number}input.txt", "wt")
f.close()

tin = open("Utilities/Templates/day_template.txt", "rt")
pout = open(f"Day{number}/day{number}.py", "w")

for line in tin:
    pout.write(line.replace("<INPUTFILEHERE>", f'"day{number}input.txt"'))

tin.close()
pout.close()