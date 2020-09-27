# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh

import random
import os
import shutil

fileName = "random.txt"

num_splitFiles = 0

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


def splitFiles():
    fileCleanup()
    print("\nSplit sorting 1 Million file ..." )
    readNums = []
    f = open(fileName,'r')
    counter = 0
    global num_splitFiles
    os.mkdir('./temp/')
    for line in f:
        # print(int(line))
        counter+=1
        readNums.append(int(line))
        if (counter % 10 == 0):
            fx = open('./temp/file' + str(num_splitFiles) + '.txt','w')
            readNums = sorted(readNums)
            for i in readNums:
                fx.write(str(i) + '\n')
            readNums.clear()
            num_splitFiles+=1
    f.close()

def fileCleanup():
    if os.path.exists("file0"):
        os.remove("file0")
    if os.path.exists('./temp'):
        shutil.rmtree('./temp')

def minValListPopulator():
    for i in range(len(minValList)):
        if minValList[i] == 0:
            minValList[i] = int(FileArrList[i].getTopElm())


def sortedFileMaker():
    f = open('random1MSorted.txt', "a")
    index = minValList.index(min(minValList))
    line = min(minValList)
    minValList[index] = 0
    f.write(str(line) + '\n')
    f.close()

# Creating Split Files
splitFiles()

# Print no. of files created after splitting
print('No. of Temp Split Files: ',num_splitFiles)

# Initializing list to hold minimum values from all the sub files
minValList = [0 for i in range(num_splitFiles)]  # a list to contain minimum values from all the files

# List to hold opened files as FileArr class instances
FileArrList = [FileArr('./temp/file' + str(i) + '.txt') for i in range(num_splitFiles)]


def sort():
    # populate sorter array for first time
    minValListPopulator()

    # clean older sorted file
    if os.path.exists('random1MSorted.txt'):
        os.remove('random1MSorted.txt')

    # sort all files until sorter array has all elements as 100
    while True:
        if(min(minValList) == 100):
            break
        sortedFileMaker()
        minValListPopulator()
        # print(minValList)

    # close all temp files and remove them
    for i in FileArrList:
        i.closeFile()
    # fileCleanup()

# Calling Main Sorting Function
sort()