# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh 300156800


"""
Install MinHash using:

pip install datasketch
"""

import random
import os
import shutil
import sys
from datasketch import MinHash

# globals
nums_per_file = 1000

num_splitFiles_A = 0

num_splitFiles_B = 0

randoms_to_create = 1000000

random.seed(10)

setA = set([])
setB = set([])

tempJaccardVal = 0.0


class FileArr:
    def __init__(self, fileName):
        self.fileVar = self.openFile(fileName)
        self.headCounter = 0

    def getTopElm(self):
        number = self.fileVar.readline()
        if(number == ''):
            return None
        return int(number)
    
    def openFile(self, fileName):
        return open(fileName,'r')

    def closeFile(self):
        self.fileVar.close()


def fileWrite1(fileName1):
    f = open(fileName1, "w")
    print("Writing 1 Million A.txt file ...")
    for i in range(randoms_to_create):
        line = str(random.randint(1,10000000))
        f.write(line + '\n')
        # print(line) 
    f.close()

def fileWrite2(fileName2):
    f = open(fileName2, "w")
    print("Writing 1 Million B.txt file ...")
    for i in range(randoms_to_create):
        line = str(random.randint(1,10000000))
        f.write(line + '\n')
        # print(line) 
    f.close()

def tempFileCleanup():
    if os.path.exists("A.txt"):
        os.remove("A.txt")
    if os.path.exists('./tempA'):
        shutil.rmtree('./tempA')

    if os.path.exists("B.txt"):
        os.remove("B.txt")
    if os.path.exists('./tempB'):
        shutil.rmtree('./tempB')
   

def splitFilesA(fileName1):
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
    # Print no. of files created after splitting
    print('\nNo. of split files created for A.txt : ',num_splitFiles_A)


def splitFilesB(fileName2):
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
    print('\nNo. of split files created for B.txt : ',num_splitFiles_B)

def setMakerA(fileArrList):
    if(len(setA) != 0):
        setA.clear()
    for i in fileArrList:
        if i.getTopElm() != None:
            setA.add(i.getTopElm())
            print(setA)
        else:
            continue

def setMakerB(fileArrList):
    if(len(setB) != 0):
        setB.clear()
    for i in fileArrList:
        if i.getTopElm() != None:
            setB.add(i.getTopElm())
        else:
            continue

def jaccardCal(setA,setB):
    # return (len(setA & setB) / len(setA | setB))
    return (len(setA.intersection(setB)) / len(setA.union(setB)))

def genJaccard(file1,file2):
    global tempJaccardVal
    # Creating Split Files
    splitFilesA(file1)
    splitFilesB(file2)

    FileArrList1 = [FileArr('./tempA/file' + str(i) + '.txt') for i in range(num_splitFiles_A)]
    FileArrList2 = [FileArr('./tempB/file' + str(i) + '.txt') for i in range(num_splitFiles_B)]

    print("\nStarting Calculation: \n")
    for i in range(1):
        
        setMakerA(FileArrList1)
        setMakerB(FileArrList2)

        # if i == 0:
        #     print('Set A:', setA)
        # print('Set B:', setB)


        tempJaccardVal += jaccardCal(setA,setB)

    print('Estimated Jaccard Value: ', tempJaccardVal)
    for i in range(len(FileArrList1)):
        FileArrList1[i].closeFile()
        FileArrList2[i].closeFile()
        


def main():
    fileName1 = "A.txt"
    fileName2 = "B.txt"
    
    # Clean older temp files
    tempFileCleanup()

    # write the 1 M random num file
    fileWrite1(fileName1)
    fileWrite2(fileName2)


    genJaccard(fileName1,fileName2)

    # print('\n\nEstimated Jaccard Value', jaccardValue)



main()