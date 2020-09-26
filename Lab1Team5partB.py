# Team Members:
# Chinmay Sharma 300157594
# Sahib 

import random

fileName = "random1M.txt"

random.seed(10)

f = open(fileName, "w")
print("Writing 1 Million file ...")
for i in range(100):
    line = str(random.randint(1,99))
    f.write(line + '\n')
    # print(line) 
f.close()

print("\nReading and sorting 1 Million file ..." )
readNums = []
f = open(fileName,'r')
for line in f:
    # print(int(line))
    readNums.append(int(line))
f.close()

print(sorted(readNums))