class AVLNode:
    def __init__(self,val):
        self.val= val
        self.left= None
        self.right= None
        self.height= 1

class AVLTree:
    
    def infix(self,start,temp):
        if not start:
            return
        self.infix(start.left,temp)
        temp.append(start.val)
        self.infix(start.right,temp)
        return temp
   
    def getHeight(self,start):
        if not start:
            return 0
        return start.height
    
    def getBalance(self,start):
        if not start:
            return 0
        return self.getHeight(start.left)-self.getHeight(start.right)

    def RRrotation(self,db):
        newRoot= db.right
        db.right= db.right.left
        newRoot.left= db
        
        db.height= 1+ max(self.getHeight(db.left),self.getHeight(db.right))
        newRoot.height= 1+ max(self.getHeight(newRoot.left),self.getHeight(newRoot.right))

        return newRoot

    def LLrotation(self,db):
        newRoot= db.left
        db.left= db.left.right
        newRoot.right= db
        
        db.height= 1+ max(self.getHeight(db.left),self.getHeight(db.right))
        newRoot.height= 1+ max(self.getHeight(newRoot.left),self.getHeight(newRoot.right))

        return newRoot

    def insertNode(self,start,key):
        if not start:
            return AVLNode(key)
        
        elif key<start.val:
            start.left= self.insertNode(start.left,key)
            
        elif key>start.val:
            start.right= self.insertNode(start.right,key)
        
        start.height= 1+ max(self.getHeight(start.left),self.getHeight(start.right))

        balance= self.getBalance(start)
        
        if balance>1 and key<start.left.val:
            return self.LLrotation(start)
        if balance>1 and key> start.left.val:
            start.left=self.RRrotation(start.left)
            return self.LLrotation(start)
    
        if balance<1 and key>start.right.val:
            return self.RRrotation(start)
        if balance<1 and key<start.right.val:
            start.right=self.LLrotation(start.right)
            return self.RRrotation(start)
        return start
   
    def minNode(self,start):
        t= start
        while t.left:
            t=t.left
        return t

    def deleteNode(self,start,key):
        if not start:
            return
        if key<start.val:
            start.left= self.deleteNode(start.left,key)
        elif key>start.val:
            start.right= self.deleteNode(start.right,key)
        else:
            if not start.left:
                temp= start.right
                start= None
                return temp
            elif not start.right:
                temp= start.left
                start=None
                return temp
            
            temp= self.minNode(start.right)
            start.val=temp.val
            start.right= self.deleteNode(start.right,temp.val)

        if not start:
            return
        
        start.height= 1+ max(self.getHeight(start.left),self.getHeight(start.right))
        balance= self.getBalance(start)

        if balance>1 and self.getBalance(start.left)>=0:
            start= self.LLrotation(start)
        if balance>1 and self.getBalance(start.left)<0:
            start.left= self.RRrotation(start.left)
            start= self.LLrotation(start)
        if balance<-1 and self.getBalance(start.right)<=0:
            start= self.RRrotation(start)
        if balance<-1 and self.getBalance(start.right)>0:
            start.right= self.LLrotation(start.right)
            start=self.RRrotation(start)   
        return start
    

avt= AVLTree()
root= None
root= avt.insertNode(root,10)
root= avt.insertNode(root,20)
root= avt.insertNode(root,30)
root= avt.insertNode(root,40)
root= avt.insertNode(root,50)
print(avt.infix(root,[]))
root= avt.deleteNode(root,10)
print(avt.infix(root,[]))
print(root.val)


