from collections import deque
from Stack import Stack

count= [10]
class Node:
    def __init__(self,val):
        self.val= val
        self.left= None
        self.right= None

class BinarySearchTree:
    def __init__(self,val) -> None:
        self.root= Node(val)
    
    def infix(self,start,temp):
        if not start:
            return
        self.infix(start.left,temp)
        temp.append(start.val)
        self.infix(start.right,temp)
        return temp
    
    def prefix(self,start,temp):
        if not start:
            return
        temp.append(start.val)
        self.prefix(start.left,temp)
        self.prefix(start.right,temp)
        return temp
    
    def postfix(self,start,temp):
        if not start:
            return
        self.postfix(start.left,temp)
        self.postfix(start.right,temp)
        temp.append(start.val)
        return temp
    
    def insert(self,start,val):
        if not start:
            return
        elif val<start.val:
            if not start.left:
                start.left= Node(val)
                return
            self.insert(start.left,val)
        
        elif val>start.val:
            if not start.right:
                start.right= Node(val)
                return
            self.insert(start.right,val)

    def minNode(self,start):
        t= start
        while t.left:
            t= t.left
        return t
    
    def iterativePreorderTraversal(self):
        t= self.root
        trav= []
        stack= Stack()
        while t or not stack.check_empty():
            if t:
                trav.append(t.val)
                stack.push_item(t)
                t=t.left
            else:
                t= stack.pop()
                t= t.right
        return trav
    
    def Search(self,start,key):
        if not start:
            return
        else:
            if key>start.val:
                self.Search(start.right,key)
            elif key<start.val:
                self.Search(start.left,key)
            elif key==start.val:
                print("Value Found")
    
    def breadthFirstSearch(self,start):
        temp= []
        queue = deque([])
        queue.append(start)

        while len(queue)!=0:
            given_val= queue.popleft()
            temp.append(given_val.val)

            if given_val.left:
                queue.append(given_val.left)
            if given_val.right:
                queue.append(given_val.right)
        return temp
    
    def delNode(self,start,key):
        if not start:
            return 
        if key<start.val:
            start.left= self.delNode(start.left,key)    
        elif key>start.val:
            start.right= self.delNode(start.right,key)
        else:
            if not start.left:
                temp= start.right
                start= None
                return temp
            
            elif not start.right:
                temp= start.left
                start= None
                return temp
            
            temp= self.minNode(start.right)
            start.val=temp.val
            start.right= self.delNode(start.right,temp.val)
        
        return start

    def displayBST(self,start,space):
        if not start:
            return
        space+=count[0]
        self.displayBST(start.right,space)
        print()
        for i in range(count[0],space):
            print(end="-")
        print(start.val)
        self.displayBST(start.left,space)           

    def completeBST(self):
        temp= self.breadthFirstSearch(self.root)
        num=2
        spc=8
        print(" "*(len(temp)),temp[0])  
        for i in range(1,len(temp),2):
            if i+2>= len(temp):
                break
            print(" "*spc,temp[i]," "*num,temp[i+1],end="  ")
            spc-=4
            if temp[i+2]<temp[i+1]:
                print()
 
    def predecessor(self,start):
        temp = self.infix(start,[])
        for i in range(len(temp)):
            if i==0:
                print("Inorder predecessor of ",temp[i],"does not exist")
            if i==(len(temp)-1):
                break
            else:
                print("Inorder predecessor of ",temp[i+1],"is ",temp[i])
               
bst= BinarySearchTree(40)
bst.insert(bst.root,10)
bst.insert(bst.root,11)  
bst.insert(bst.root,5)
bst.insert(bst.root,2)
bst.insert(bst.root,50)
bst.insert(bst.root,49)
bst.insert(bst.root,47)
bst.insert(bst.root,52)
bst.insert(bst.root,72)
# print(bst.infix(bst.root,[]))
# bst.predecessor(bst.root)
# bst.delNode(bst.root,72)
# print(bst.infix(bst.root,[]))
# bst.Search(bst.root,50)
# print(bst.prefix(bst.root,[]))
# print(bst.iterativePreorderTraversal())
# print(bst.breadthFirstSearch(bst.root))
# bst.delNode(bst.root,40)
# bst.displayBST(bst.root,0)
# print(bst.infix(bst.root,[]))
# print(bst.breadthFirstSearch(bst.root))
# print(bst.breadthFirstSearch(bst.root))
# print(bst.infix(bst.root,[]))
print(bst.infix(bst.root,[]))
print(bst.breadthFirstSearch(bst.root))