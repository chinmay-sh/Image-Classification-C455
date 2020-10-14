# Team Members:
# Chinmay Sharma 300157594
# Sahibdeep Singh 300156800

from datasketch import MinHash


# sets
A = {19,2,14,16,19,1,7,15,16,9,21,6,2,17,16,11,3,8,24}

B = {12,2,14,5,20,11,13,14,10,2982,9,24,16,22,110,21,12,5,15}

# print(len(A))

def genJaccard(setA,setB):
    # return (len(setA & setB) / len(setA | setB))
    return (len(setA.intersection(setB)) / len(setA.union(setB)))

print("Jaccard Similarity Value:", genJaccard(A,B))


m1, m2 = MinHash(),MinHash()

for i in A:
    m1.update(str(i).encode('utf8'))
for i in B:
    m2.update(str(i).encode('utf8'))

print("Estimated Jaccard for A.txt and B.txt is", m1.jaccard(m2))