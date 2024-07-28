class Queue:
    def __init__(self):
        self.rear=self.front=0
        self.queue= []
        
    def isEmpty(self):
        if self.rear==self.front:
            return True
        else:
            return False

    def enqueue(self,val):
        self.queue.append(val)
        self.rear+=1
        
    
    def dequeue(self):
        if not self.isEmpty():
            self.front+=1
            return self.queue.pop()
        else:
            return 'Queue is Empty'

    def display(self):
        if not self.isEmpty():
            for i in self.queue:
                print(i)
        

# q1= Queue()
# q1.enqueue(1)
# q1.enqueue(1)
# q1.enqueue(1)
# q1.display()
# print("------------------------------")
# print(q1.dequeue())
# print(q1.dequeue())
# print(q1.dequeue())

