class Stack:
    
    def __init__(self):
        self.stack= []
    
    def push_item(self,item):
        self.stack.append(item)
   
    def pop(self):
        if(self.check_empty()):
            return "Stack is Empty"
        return self.stack.pop()
   
    def check_empty(self,):
        return len(self.stack)==0

# st1= Stack()
# my_stack=st1.create_stack()
# st1.push_item(my_stack,str(1))
# st1.push_item(my_stack,str(2))
# st1.push_item(my_stack,str(3))
# st1.push_item(my_stack,str(4))
# print("Popped item is:",st1.pop(my_stack))
