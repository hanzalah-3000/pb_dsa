class Node:
    def __init__(self,val):
        self.next= None
        self.val= val

class LinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
        self.size= 0
    
    def addAddHead(self,val):
        nn= Node(val)
        
        if (not self.head):
            self.head= nn
            self.tail=nn
        
        else:
            nn.next=self.head
            self.head= nn
        self.size+=1
   
    def addTail(self,val):
        nn= Node(val)

        self.tail.next=nn
        self.tail=nn

        self.size+=1
    
    def AddatIndex(self,val,index):
        nn= Node(val)
        cur=self.head
        for i in range(index-1):
            cur=cur.next
        temp=cur.next
        cur.next=nn
        nn.next=temp
        self.size+=1

    def displayLinkedList(self):
    
        if self.head is None:
            print("List is empty")
        else:
            
            dl=[]
            cur= self.head
            for i in range(self.size):
                dl.append(cur.val)
                cur=cur.next
            print(dl)  

    def createLoop(self,index):
        cur=self.head
        temp= self.head.next.next
        for i in range(index):
            cur=cur.next
        cur.next= temp

    def detectLoop(self):
        temp= self.head
        cur= self.head

        while temp:
            temp=temp.next
            cur=cur.next
            if cur.next:
                cur=cur.next
            if temp==cur:
                return True
        return False 

    def reverseLinkedList(self):
        q= None
        r= None
        p= self.head

        for i in range(self.size):
            r=q
            q=p
            p=p.next
            q.next= r
        self.head= q

    def delDuplicateNode(self):
        cur= self.head
        while cur and cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
    
    

    def searchNode(self,key):
        temp= self.head
        index=0
        while temp:
            if key==temp.val:
                return index
            temp= temp.next
            index +=1
        return -1
    
    def addAtSorted(self,key):
        nn= Node(key)
        p=q=self.head

        while p and p.val<key:
            q=p
            p=p.next
       
        if p== self.head:
            nn.next=self.head
            self.head=nn
            self.size+=1
            return
       
        elif q==self.tail:
            q.next=nn
            self.tail=nn
            self.size+=1
            return
       
        q.next=nn
        nn.next=p
        self.size+=1



l1= LinkedList()
l1.addAddHead(4)
l1.addAddHead(3)
l1.addAddHead(2)
l1.addAddHead(1)
l1.displayLinkedList()
l1.displayLinkedList()
l1.addAtSorted(10)
l1.addAtSorted(9)
l1.addAtSorted(0)
l1.displayLinkedList()
# l1.addTail(2)
# l1.addTail(8)
# l1.displayLinkedList()
# l1.AddatIndex(15,2)
# l1.displayLinkedList()
# l1.reverseLinkedList()
# l1.displayLinkedList()
# print(l1.searchNode(11))
