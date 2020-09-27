# Team Members:
# Chinmay Sharma 300157594
# Sahib 

import random
import os

fileName = "random.txt"

random.seed(10)

def fileWrite():
    f = open(fileName, "w")
    print("Writing 1 Million file ...")
    for i in range(100):
        line = str(random.randint(1,99))
        f.write(line + '\n')
        # print(line) 
    f.close()

def sortSmallArr(arr):
    return sorted(arr)

def readAndSplitFile():
    print("\nReading and split 1 Million file ..." )
    readNums1000 = []
    f = open(fileName,'r')
    counter = 0
    fileCounter = 0
    for line in f:
        # print(int(line))
        if (counter % 10 == 0 and counter != 0):
            fx = open('file' + str(fileCounter) + '.txt','w')
            for i in readNums1000:
                fx.write(str(i) + '\n')
            readNums1000.clear()
        readNums1000.append(int(line))
        counter+=1
    f.close()
    

readAndSplitFile()