class Nodes:
    def __init__(self,val) :
        self.value= val
        self.next= None
        self.prev= None

class LinkedList:
    def __init__(self) :
        self.size=0
        self.tail= None
        self.head= None
    
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
    
    def insertionAtTail(self,val):
        nn=Nodes(val)
        if self.head is None:
            self.head=nn
            self.tail=nn
        
        else:
            nn.prev= self.tail
            self.tail.next= nn
            self.tail=nn
        self.size+=1
    
    def insertionAtIndex(self,value,index):
        cur=self.head
        for i in range(index-1):
            cur=cur.next
        
        nn= Nodes(value)
        
        nextnode= cur.next
        
        cur.next=nn
        nn.prev=cur

        nn.next=nextnode
        nextnode.prev= nn

        self.size+=1
      


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

    def delAtIndex(self,index):
        cur= self.head
        if(index>self.size):
            print("Index is higher")
            return
        elif self.head is None:
            print("List is Empty")
        
        elif(index==0):
            self.head=cur.next
            cur=None
        
        elif(index==(self.size-1)):
            cur=self.tail.prev
            cur.next=None
            cur=self.tail
            
        elif index!=0:
            for i in range(index-1):
                cur= cur.next
            new_next= cur.next.next
            cur.next= None
            cur.next= new_next
        
        self.size-=1

    def getValue(self,index):
        cur= self.head

        if index> (self.size-1):
            print("Index is incorrect")

        elif index==0:
            print(cur.value)

        elif index!=0:
            for i in range(index):
                cur=cur.next
            print(cur.value)
    
    def reverseLinkList(self):
        temp=None
        cur= self.head
        while cur:
            temp=cur.prev
            cur.prev=cur.next
            cur.next=temp
            cur= cur.prev
        self.head=temp.prev
    
    def traverse(self):
        cur=self.head
        for i in range(self.size):
            cur=cur.next
                                                                        
# l1= LinkedList()
# l1.insertionAtHead(1)
# l1.insertionAtHead(2)
# l1.insertionAtHead(3)
# l1.insertionAtHead(4)
# l1.displayLinkedList()
# l1.insertionAtIndex(7,1)
# l1.displayLinkedList()
# l1.delAtIndex(2)
# l1.displayLinkedList()
# l1.getValue(3) 
# l1.reverseLinkList()
# l1.displayLinkedList()