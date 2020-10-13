# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh 300156800

import random
import os
import shutil

fileName1 = "A.txt"
fileName2 = "B.txt"

nums_per_file = 1000

num_splitFiles_A = 0

num_splitFiles_B = 0

randoms_to_create = 1000000

random.seed(10)

setA = set([])
setB = set([])

jaccardValue = 0

class FileArr:
    def __init__(self, fileName):
        self.fileVar = self.openFile(fileName)
        self.headCounter = 0

    def getList(self):
        return [line for line in self.fileVar.readlines()]
    
    def openFile(self, fileName):
        return open(fileName,'r')
    
    def closeFile(self):
        self.fileVar.close()

def genJaccard(setA,setB):
    # return (len(setA & setB) / len(setA | setB))
    return (len(setA.intersection(setB)) / len(setA.union(setB)))

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

def tempFileCleanupA():
    if os.path.exists("A.txt"):
        os.remove("A.txt")
    if os.path.exists('./tempA'):
        shutil.rmtree('./tempA')

def tempFileCleanupB():
    if os.path.exists("B.txt"):
        os.remove("B.txt")
    if os.path.exists('./tempB'):
        shutil.rmtree('./tempB')

def splitFilesA():
    print("\nSplitting A.txt file ..." )
    A = []
    f = open(fileName1,'r')
    counter = 0
    global num_splitFiles_A
    os.mkdir('./tempA/')
    for line in f:
        # print(int(line))
        counter+=1
        A.append(int(line))
        if (counter % nums_per_file == 0):
            fx = open('./tempA/file' + str(num_splitFiles_A) + '.txt','w')
            for i in A:
                fx.write(str(i) + '\n')
            A.clear()
            num_splitFiles_A+=1
    f.close()

def splitFilesB():
    print("\nSplitting B.txt file ..." )
    B = []
    f = open(fileName2,'r')
    counter = 0
    global num_splitFiles_B
    os.mkdir('./tempB/')
    for line in f:
        # print(int(line))
        counter+=1
        B.append(int(line))
        if (counter % nums_per_file == 0):
            fx = open('./tempB/file' + str(num_splitFiles_B) + '.txt','w')
            for i in B:
                fx.write(str(i) + '\n')
            B.clear()
            num_splitFiles_B+=1
    f.close()

def setMakerA(partFile):
    if(len(setA) != 0):
        setA.clear()
    listToLoad = partFile.getList()
    for i in listToLoad:
        setA.add(i)

def setMakerB(partFile):
    if(len(setB) != 0):
        setB.clear()
    listToLoad = partFile.getList()
    for i in listToLoad:
        setB.add(i)

def splitFilesReader():
    global jaccardValue
    for i in range(num_splitFiles_A):
        partFileA = FileArr('./tempA/file' + str(i) + '.txt')
        partFileB = FileArr('./tempB/file' + str(i) + '.txt')

        setMakerA(partFileA)
        setMakerB(partFileB)

        partFileA.closeFile()
        partFileB.closeFile()

        jaccardValue += genJaccard(setA,setB)


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
print('\nNo. of split files created for A.txt : ',num_splitFiles_A)

print('\nNo. of split files created for B.txt : ',num_splitFiles_B)

splitFilesReader()

print('Estimated Jaccard Value', jaccardValue)

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
