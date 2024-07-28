from collections import deque

class Node:
    def __init__(self,val):
        self.val= val
        self.left= None
        self.right= None

class BinaryTree:
    def __init__(self,val):
        self.root= Node(val)
    
    def prefix(self,start,temp):
        if not start:
            return
        temp.append(start.val)
        self.prefix(start.left,temp)
        self.prefix(start.right,temp)
        return temp
   
    def infix(self,start,temp):
        if not start:
            return
        self.infix(start.left,temp)
        temp.append(start.val)
        self.infix(start.right,temp)
        return temp
   
    def postfix(self,start,temp):
        if not start:
            return
        self.postfix(start.left,temp)
        self.postfix(start.right,temp)
        temp.append(start.val)
        return temp

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
obj= BinaryTree(1)
obj.root.left= Node(2)
obj.root.right= Node(3)
obj.root.left.left= Node(4)
obj.root.left.right= Node(5)
obj.root.right.left= Node(6)
obj.root.right.right= Node(7)
print('Prefix:  ',obj.prefix(obj.root,[]))
print('Infix:  ',obj.infix(obj.root,[]))
print('Postfix: ',obj.postfix(obj.root,[]))
print('Breadth First Search: ',obj.breadthFirstSearch(obj.root))

                

