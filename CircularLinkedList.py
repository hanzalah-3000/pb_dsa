class Nodes:
    def __init__(self,val) :
        self.value= val
        self.next= None

class CircularLinkedList:
    def __init__(self) :
        self.size=0
        self.head= None
        self.tail= None

    def insertAtHead(self,val):
        nn= Nodes(val)
        if not self.head:
            nn.next=nn
            self.head= nn
            self.tail= nn
        else:
            nn.next= self.head
            self.head=nn
            self.tail.next= nn
        self.size+=1
    
    def delAtHead(self):
        cur=self.head
        cur=cur.next
        self.head=cur
        self.tail.next= cur
        self.size-=1
   
    def delAtTail(self):
        temp= self.head
        cur= self.head
        for i in range(self.size-1):
            cur = cur.next
        
        cur.next= self.head
        self.tail=cur
        self.tail.next= temp           
        self.size-=1
   
    def delAtIndex(self,index):
        if index>self.size or index<0:           
            print("Invalid Index")
        elif index==0:
            self.delAtHead()
        elif index==self.size:
            self.delAtTail()
        else:
            cur= self.head
            for i in range(index-1):
                cur=cur.next
            cur.next=cur.next.next
            self.size-=1
            
    def insertAtIndex(self,index,val):
        nn= Nodes(val)
        if index>self.size or index<0:
            print("Invalid Index")
        elif index==0:
            self.insertAtHead(val)
        elif index==self.size:
            self.insertAtTail(val)
        else:
            cur= self.head
            for i in range(index-1):
                cur=cur.next
            nextnode=cur.next
            cur.next= nn
            nn.next= nextnode
        self.size+=1
   
    def insertAtTail(self,val):
        nn= Nodes(val)
        if not self.head:
            nn.next=nn
            self.head=nn
            self.tail-nn
        else:
            self.tail.next= nn
            nn.next= self.head
            self.tail=nn
        self.size+=1
    
    def searchNode(self,index):
        if index>self.size or index<0:
            print("Invalid Index")
        else:
            cur = self.head
            for i in range(index):
                cur=cur.next
            print(cur.value)
    
    def displayCLL(self):
        cur=self.head
        dl=[]
        for i in range(self.size):
            dl.append(cur.value)
            cur=cur.next
        print(dl)


cll= CircularLinkedList()
cll.insertAtHead(5)
cll.insertAtHead(4)
cll.insertAtHead(3)
cll.insertAtHead(2)
cll.displayCLL()
cll.insertAtIndex(1,1)
cll.insertAtIndex(3,1)
cll.displayCLL()
cll.insertAtTail(9)
cll.insertAtTail(5)
cll.displayCLL()
cll.searchNode(6)
cll.delAtIndex(7)
cll.displayCLL()