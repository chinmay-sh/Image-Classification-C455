# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh 300156800


import random
import os
import shutil

# globals

#limit to random number per split file
nums_per_file = 1000

#Number of split files for TempA folder
num_splitFiles_A = 0

#Number of split files for TempA folder
num_splitFiles_B = 0

#Number of random integers to create
randoms_to_create = 1000000

random.seed(10)

#setA and setB value
setA = set([])
setB = set([])

#this is the temporary Jaccard Value
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
    
    def getList(self):
        return [line for line in self.fileVar.readlines()]

# Writing A.txt file
def fileWrite1(fileName1):
    f = open(fileName1, "w")
    print("Writing 1 Million A.txt file ...")
    for i in range(randoms_to_create):
        line = str(random.randint(1,10000000))     #from 1 to 10000000 choose any random number
        f.write(line + '\n')
        # print(line) 
    f.close()

# Writing B.txt file
def fileWrite2(fileName2):
    f = open(fileName2, "w")
    print("Writing 1 Million B.txt file ...")
    for i in range(randoms_to_create):
        line = str(random.randint(1,10000000))     #from 1 to 10000000 choose any random number
        f.write(line + '\n')
        # print(line) 
    f.close()

#to clean up the A.txt and B.txt files and tempA and tempB folders
def tempFileCleanup():
    if os.path.exists("A.txt"):
        os.remove("A.txt")
    if os.path.exists('./tempA'):
        shutil.rmtree('./tempA')

    if os.path.exists("B.txt"):
        os.remove("B.txt")
    if os.path.exists('./tempB'):
        shutil.rmtree('./tempB')
   
#Split A.txt file into 'n' files and store them in tempA folder
def splitFilesA(fileName1):
    print("\nSplitting A.txt file ..." )
    A = []
    f = open(fileName1,'r')
    counter = 0
    global num_splitFiles_A
    os.mkdir('./tempA/')        #create a folder tempA
    for line in f:
        # print(int(line))
        counter+=1
        A.append(int(line))
        if (counter % nums_per_file == 0):
            #Open folder tempA and write a fileN.txt, where N is the number of split files, for example, file0.txt and the file1.txt and so on....
            fx = open('./tempA/file' + str(num_splitFiles_A) + '.txt','w')         
            for i in A:
                fx.write(str(i) + '\n')
            A.clear()
            num_splitFiles_A+=1
    f.close()
    # Print no. of files created after splitting
    print('\nNo. of split files created for A.txt : ',num_splitFiles_A)

#Split B.txt file into 'n' files and store them in tempB folder
def splitFilesB(fileName2):
    print("\nSplitting B.txt file ..." )
    B = []
    f = open(fileName2,'r')
    counter = 0
    global num_splitFiles_B
    os.mkdir('./tempB/')    #create a folder tempB
    for line in f:
        # print(int(line))
        counter+=1
        B.append(int(line))
        if (counter % nums_per_file == 0):
            #Open folder tempB and write a fileN.txt, where N is the number of split files, for example, file0.txt and the file1.txt and so on....
            fx = open('./tempB/file' + str(num_splitFiles_B) + '.txt','w')
            for i in B:
                fx.write(str(i) + '\n')
            B.clear()
            num_splitFiles_B+=1
    f.close()
    # Print no. of files created after splitting
    print('\nNo. of split files created for B.txt : ',num_splitFiles_B)

def jaccardCal(setA,setB):
    # return (len(setA & setB) / len(setA | setB))
    if(len(setA) == 0 and len(setB) == 0):
        return 1
    return (len(setA.intersection(setB)) / len(setA.union(setB)))

def genJaccard(file1,file2):
    global tempJaccardVal
    # Creating Split Files
    splitFilesA(file1)
    splitFilesB(file2)

    FileArrList1 = [FileArr('./tempA/file' + str(i) + '.txt') for i in range(num_splitFiles_A)]
    FileArrList2 = [FileArr('./tempB/file' + str(i) + '.txt') for i in range(num_splitFiles_B)]

    print("\nStarting Calculation: \n")
    for i in range(nums_per_file):
        if(len(setA) != 0):
            setA.clear()

        if(len(setB) != 0):
            setB.clear()

        for x in range(num_splitFiles_A):
            setA.add(FileArrList1[x].getTopElm())
            setB.add(FileArrList2[x].getTopElm())

        tempJaccardVal += jaccardCal(setA,setB)

    print('Estimated Jaccard Value: ',tempJaccardVal)
    for i in range(len(FileArrList1)):
        FileArrList1[i].closeFile()
        FileArrList2[i].closeFile()
        


def main():
    #file name for A.txt
    fileName1 = "A.txt"
    #file name for B.txt
    fileName2 = "B.txt"
    
    # Clean older temp files
    tempFileCleanup()

    # write the 1 M random num file
    fileWrite1(fileName1)   # As A.txt
    fileWrite2(fileName2)   # As B.txt

    #get the Jaccard value for A.txt and B.txt file from files of tempA and tempB folder
    genJaccard(fileName1,fileName2)


main()
