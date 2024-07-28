from LinkedList import LinkedList

class HashChain:
    def __init__(self) :
        self.size= 10
        self.table=[0]*self.size
        for i in range(self.size):
            self.table[i]= LinkedList()

    def hashCode(self,key):
        return key%10

    def insert(self,key):
        i= self.hashCode(key)
        self.table[i].addAtSorted(key)
    
    def display(self):
        for i in range(self.size):
            print('[',i,']',end='')
            self.table[i].displayLinkedList()

    def search(self,key):
        i= self.hashCode(key)
        return self.table[i].searchNode(key)!=-1

H= HashChain()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(34)
H.insert(86)
H.insert(28)
H.display()
print(H.search(54))

