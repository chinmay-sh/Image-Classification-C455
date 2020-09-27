# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh

import random
import os
import shutil

fileName = "random1M.txt"

num_splitFiles = 0

nums_per_file = 1000

randoms_to_create = 1000000

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
    for i in range(randoms_to_create):
        line = str(random.randint(1,99))
        f.write(line + '\n')
        # print(line) 
    f.close()


def splitFiles():
    tempFileCleanup()
    print("\nSplitting 1 Million file ..." )
    readNums = []
    f = open(fileName,'r')
    counter = 0
    global num_splitFiles
    os.mkdir('./temp/')
    for line in f:
        # print(int(line))
        counter+=1
        readNums.append(int(line))
        if (counter % nums_per_file == 0):
            fx = open('./temp/file' + str(num_splitFiles) + '.txt','w')
            readNums = sorted(readNums)
            for i in readNums:
                fx.write(str(i) + '\n')
            readNums.clear()
            num_splitFiles+=1
    f.close()

def tempFileCleanup():
    if os.path.exists("file0"):
        os.remove("file0")
    if os.path.exists('./temp'):
        shutil.rmtree('./temp')

def minValListPopulator():
    for i in range(len(minValList)):
        if minValList[i] == 0:
            minValList[i] = int(FileArrList[i].getTopElm())


def sortedFileMaker(f):
    index = minValList.index(min(minValList))
    line = min(minValList)
    minValList[index] = 0
    f.write(str(line) + '\n')

def sort():
    # populate sorter array for first time
    minValListPopulator()

    # clean older sorted file
    if os.path.exists('random1MSorted.txt'):
        os.remove('random1MSorted.txt')

    # sort all files until sorter array has all elements as 100
    f = open('random1MSorted.txt', "a")
    while True:
        if(min(minValList) == 100):
            break
        sortedFileMaker(f)
        minValListPopulator()
        # print(minValList)
    f.close()

    # close all temp files and remove them
    for i in FileArrList:
        i.closeFile()
    # tempFileCleanup()

    print('\nSorting Complete!')

# Clean older temp files
tempFileCleanup()

# write the 1 M random num file
fileWrite()

# Creating Split Files
splitFiles()

# Print no. of files created after splitting
print('\nNo. of split files created: ',num_splitFiles)

# Initializing list to hold minimum values from all the sub files
minValList = [0 for i in range(num_splitFiles)]  # a list to contain minimum values from all the files
print('\nSize of sorting array holding min vals:',len(minValList))

# List to hold opened files as FileArr class instances
FileArrList = [FileArr('./temp/file' + str(i) + '.txt') for i in range(num_splitFiles)]

# Calling Main Sorting Function
sort()