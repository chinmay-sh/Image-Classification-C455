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



# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh 300156800

"""
import random
import os
import shutil


fileName1 = "A.txt"
fileName2 = "B.txt"

num_splitFiles = 0

nums_per_file = 1000

randoms_to_create = 1000000

random.seed(10)


class FileArr:
    def __init__(self, fileName1):
        self.fileVar = self.openFile(fileName1)
        self.headCounter = 0

    def __init__1(self, fileName2):
        self.fileVar = self.openFile(fileName2)
        self.headCounter = 0

    def getTopElm(self):
        number = self.fileVar.readline()
        if(number == ''):
            return '100'
        return number
    
    def openFile1(self, fileName1):
        return open(fileName1,'r')
    
    def openFile2(self, fileName2):
        return open(fileName2,'r')

    def closeFile(self):
        self.fileVar.close()

def fileWrite1():
    f = open(fileName1, "w")
    print("Writing A.txt file ...")
    for i in range(randoms_to_create):
        line = str(random.randint(1,10000000))
        f.write(line + '\n')
        # print(line) 
    f.close()

def fileWrite2():
    f = open(fileName2, "w")
    print("Writing B.txt file ...")
    for i in range(randoms_to_create):
        line = str(random.randint(1,10000000))
        f.write(line + '\n')
        # print(line) 
    f.close()

def tempFileCleanupA():
    if os.path.exists("file0"):
        os.remove("file0")
    if os.path.exists('./tempA'):
        shutil.rmtree('./tempA')

def tempFileCleanupB():
    if os.path.exists("file0"):
        os.remove("file0")
    if os.path.exists('./tempB'):
        shutil.rmtree('./tempB')

def minValListPopulator():
    for i in range(len(minValList)):
        if minValList[i] == 0:
            minValList[i] = int(FileArrList[i].getTopElm())

def splitFilesA():
    tempFileCleanupA()
    print("\nSplitting A.txt file ..." )
    A = []
    f = open(fileName1,'r')
    counter = 0
    global num_splitFiles
    os.mkdir('./tempA/')
    for line in f:
        # print(int(line))
        counter+=1
        A.append(int(line))
        if (counter % nums_per_file == 0):
            fx = open('./tempA/file' + str(num_splitFiles) + '.txt','w')
            for i in A:
                fx.write(str(i) + '\n')
            A.clear()
            num_splitFiles+=1
    f.close()

def splitFilesB():
    tempFileCleanupB()
    print("\nSplitting B.txt file ..." )
    B = []
    f = open(fileName1,'r')
    counter = 0
    global num_splitFiles
    os.mkdir('./tempB/')
    for line in f:
        # print(int(line))
        counter+=1
        B.append(int(line))
        if (counter % nums_per_file == 0):
            fx = open('./tempB/file' + str(num_splitFiles) + '.txt','w')
            for i in B:
                fx.write(str(i) + '\n')
            B.clear()
            num_splitFiles+=1
    f.close()


# Clean older temp files
tempFileCleanupA()
tempFileCleanupB()

# write the 1 M random num file
fileWrite1()
fileWrite2()

# Creating Split Files
splitFilesA()
splitFilesB()

# Print no. of files created after splitting
print('\nNo. of split files created: ',num_splitFiles)


"""
