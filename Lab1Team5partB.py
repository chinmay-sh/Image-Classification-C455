# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh

import random
import os
import shutil

fileName = "random.txt"

fileCounter = 0

random.seed(10)

class FileArr:
    def __init__(self, fileName):
        self.fileVar = self.openFile(fileName)
        self.headCounter = 0

    def getTopElm(self):
        number = self.fileVar.readline()
        if(number == ''):
            return '100'
        return number
    
    def openFile(self, fileName):
        return open(fileName,'r')

    def closeFile(self):
        self.fileVar.close()



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

minValList = [0 for i in range(fileCounter)]  # a list to contain minimum values from all the files

print(minValList)

FileArrList = [FileArr('./temp/file' + str(i) + '.txt') for i in range(fileCounter)]

def minValListPopulator():
    for i in range(len(minValList)):
        if minValList[i] == 0:
            minValList[i] = int(FileArrList[i].getTopElm())

# f0 = FileArr('./temp/file0.txt')

# for i in range(10):
#     print(f0.getTopElm())

# f0.closeFile()


# print(FileArrList[0].getTopElm())
# print(FileArrList[1].getTopElm())
# print(FileArrList[0].getTopElm())


minValListPopulator()

print(minValList)

def sortedFileMaker():
    f = open('random1MSorted.txt', "a")
    print("Writing 1 Million sorted file ...")
    # for i in range(1):
    index = minValList.index(min(minValList))
    line = min(minValList)
    minValList[index] = 0
    f.write(str(line) + '\n')
        # print(line)
    f.close()

if os.path.exists('random1MSorted.txt'):
    os.remove('random1MSorted.txt')

for i in range(100):
    sortedFileMaker()
    minValListPopulator()
    print(minValList)

for i in FileArrList:
    i.closeFile()