# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh 300156800

import random


fileName1 = "A.txt"
fileName2 = "B.txt"

nums_per_file = 1000

randoms_to_create = 1000000

random.seed(10)

def fileWrite1():
    f = open(fileName1, "w")
    print("Writing 1 Million file ...")
    for i in range(randoms_to_create):
        line = str(random.randint(1,10000000))
        f.write(line + '\n')
        # print(line) 
    f.close()

def fileWrite2():
    f = open(fileName2, "w")
    print("Writing 1 Million file ...")
    for i in range(randoms_to_create):
        line = str(random.randint(1,10000000))
        f.write(line + '\n')
        # print(line) 
    f.close()

fileWrite1()
fileWrite2()
