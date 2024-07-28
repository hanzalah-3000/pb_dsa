class Contact:
    def __init__(self,name,number):
        self.name= name
        self.number= number
        self.next=None
        self.prev=None

class ContactList:
    def __init__(self):
        self.head= None
        self.tail= None
        self.size=0
    
    def addContact(self,name,number):
        nn= Contact(name,number)
    
        if not self.head:
            self.head=nn
            self.tail=nn

        else:
            q=None
            p=self.head
            
            while p and p.name<name:
                q=p
                p=p.next
            
            if p== self.head:
                nn.next=self.head
                self.head= nn
                
            elif q==self.tail:
                q.next=nn
                self.tail= nn
                
            else:
                q.next=nn
                nn.prev= q

                nn.next=p
                p.prev=nn
        self.size+=1   
        
    def deleteContact(self,name):
        p= self.head
        q=None
        while p and name!=p.name:
            q=p
            p=p.next
        if p:
            if name==p.name:
                if p==self.head:
                    self.head=self.head.next
                else:
                    q.next=p.next
                    p.prev=q
        else:
            print("Not found") 
        
        self.size-=1
    
    def searchContact(self,name):
        cur=self.head

        while cur:
            if cur.name==name:
                print(cur.name,cur.number)
                break
            cur=cur.next
        else:
            print("Not found")

    def updateContact(self,name,number):
        cur= self.head
        while cur:
            if name==cur.name:
                cur.number= number
                print('Contact Updated Successfully')
                break
            cur=cur.next
        else:
            print("Contact not Found")

    def displayContactList(self):
        cur=self.head
        while cur:
            print(cur.name,cur.number)
            cur=cur.next
    
    def returnDictionary(self):
        cur=self.head
        trav={}
        
        while cur:
            trav[cur.name]= cur.number
            cur=cur.next
        return trav
    
    def BST(self,A,dic,start,end,key,mid):
    
        if key<A[mid]:
            mid//=2
            self.BST(A,dic,start,mid-1,key,mid)

        elif key>A[mid]:
            self.BST(A,dic,mid+1,end,key,mid+1)

        else:
            print(A[mid],dic[A[mid]])
    
    def searchContactBST(self,name):
        trav= self.returnDictionary()
        index= list(trav)      
        self.BST(index,trav,index[0],len(index)-1,name,len(index)//2)

    
c1= ContactList()
c1.addContact("zeeshan","004875093")
c1.addContact("ali","053905093")
c1.addContact("usama","053048753")
c1.addContact("nouman","0454093")
c1.addContact("ahmed","023909093")
c1.addContact("farhan","45239093")
c1.addContact("bilal","02393239093")
c1.addContact("haroon","02393239093")
c1.addContact("hasnain","07387939093")
print('_______________________________')
print('Displaying Phonebook')
print('_______________________________')
c1.displayContactList()
print('_______________________________')
print('Deleting ahmed, bilal and zeeshan')
c1.deleteContact("zeeshan")
c1.deleteContact("ahmed")
c1.deleteContact("bilal")
print('_______________________________')
c1.displayContactList()
print('_______________________________')
print('Searching a contact')
print('_______________________________')
c1.searchContact('usama')
print('_______________________________')            
print("Updating a Contact")
print('_______________________________')
c1.updateContact('haroon','11111111')
c1.displayContactList()
print("_______________________________")
print("Searching by using BST")
print("_______________________________")
try:
    c1.searchContactBST("haroon")
except:
    print("Not Found")