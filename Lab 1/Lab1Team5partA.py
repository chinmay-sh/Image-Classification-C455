# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh 300156800

import random

fileName = "random.txt"

f = open(fileName, "w")
print("Writing file ...")
for i in range(100):
    line = str(random.randint(1,99))
    f.write(line + '\n')
    # print(line) 
f.close()

print("\nReading file ..." )
readNums = []
f = open(fileName,'r')
for line in f:
    # print(int(line))
    readNums.append(int(line))
f.close()

print(sorted(readNums))