

class Nodes:
    def __init__(self,val) :
        self.value= val
        self.next= None
        self.prev= None

class LinkedList:
    def __init__(self) :
        self.size=0
        self.head= None
        self.tail= None

    def insertionAtHead(self,val):
        nn= Nodes(val)
        if self.head is None:
            self.head=nn
            self.tail=nn
        
        else:
            nn.next= self.head
            self.head.prev= nn
            self.head=nn
        
        self.size+=1
    def DuplicateNode(self):
        temp1=None


        temp1= self.head
        

        while (temp1 and temp1.next):
            temp2= temp1

            if temp1.value== temp1.next.value:
                return True
                
            temp1= temp1.next
        else:
            return False


            
    def displayLinkedList(self):
        
        if self.head is None:
            print("List is empty")
        else:
            dl=[]
            cur= self.head
            for i in range(self.size):
                dl.append(cur.value)
                cur=cur.next
            print(dl)

l1= LinkedList()
l1.insertionAtHead(2)
l1.insertionAtHead(3)
l1.insertionAtHead(5)
l1.insertionAtHead(9)
l1.insertionAtHead(9)
l1.displayLinkedList()
print(l1.DuplicateNode())