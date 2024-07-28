class HashingLinearProbe:
    def __init__(self):
        self.size= 10
        self.table= [0]*self.size
    
    def hashCode(self,key):
        return key % self.size

    def linearProbe(self,elem):
        i= self.hashCode(elem)
        j=0

        while self.table[i+j]!=0:
            j+=1
        
        return self.hashCode(i+j)
    
    def insert(self,elem):
        i= self.hashCode(elem)

        if self.table[i]==0:
            self.table[i]=elem
        else:
            i=self.linearProbe(elem)
            self.table[i]=elem

    def search(self,key):
        i= self.hashCode(key)
        j=0

        while self.table[i+j]!=key:
            if self.table[i+j]==0:
                return False
            j+=1
        
        return True

    def display(self):
        print(self.table)

h1= HashingLinearProbe()
h1.insert(19)
h1.insert(8)
h1.insert(27)
h1.insert(42)
h1.insert(22)
h1.insert(12)
h1.insert(22)
h1.insert(24)
h1.insert(91)
h1.display()
print(h1.search(10))