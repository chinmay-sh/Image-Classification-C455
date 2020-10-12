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


# strategy for partB
# testA1 = {19,2,14,16,19,1,7,15,16,9}
# testB1 = {12,2,14,5,20,11,13,14,10,2982}

# testA2 = {21,6,2,17,16,11,3,8,24}
# testB2 = {9,24,16,22,110,21,12,5,15}

# x = genJaccard(testA1,testB1)
# y = genJaccard(testA2,testB2)
# print(x)
# print(y)

# print(x + y)