# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh

import random
import os
import shutil

fileName = "random.txt"

fileCounter = 0

random.seed(10)

def fileWrite():
    f = open(fileName, "w")
    print("Writing 1 Million file ...")
    for i in range(100):
        line = str(random.randint(1,99))
        f.write(line + '\n')
        # print(line) 
    f.close()


def readAndSplitSortFile():
    fileCleanup()
    print("\nReading and split sorting 1 Million file ..." )
    readNums = []
    f = open(fileName,'r')
    counter = 0
    global fileCounter
    os.mkdir('./temp/')
    for line in f:
        # print(int(line))
        counter+=1
        readNums.append(int(line))
        if (counter % 10 == 0):
            fx = open('./temp/file' + str(fileCounter) + '.txt','w')
            readNums = sorted(readNums)
            for i in readNums:
                fx.write(str(i) + '\n')
            readNums.clear()
            fileCounter+=1
    f.close()

def fileCleanup():
    if os.path.exists("file0"):
        os.remove("file0")
    if os.path.exists('./temp'):
        shutil.rmtree('./temp')


readAndSplitSortFile()

print(fileCounter)

minValList = ['X' for i in range(fileCounter)]

# def minValListPopulator():

