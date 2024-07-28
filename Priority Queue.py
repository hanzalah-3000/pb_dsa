class PriorityQueue:
    def __init__(self):
        self.queue= []
    
    def __str__(self) :
        return ' '.join([str(i) for i in self.queue])
    
    def Empty(self):
        if len(self.queue)==0:
            return True
        return False
    
    def Insert(self,val):
        self.queue.append(val)

    def Delete(self):
        max=0
        for i in range(len(self.queue)):
            if self.queue[i]>self.queue[max]:
                max= i
        
        item= self.queue[max]

        del self.queue[max]

        return item

q1= PriorityQueue()
q1.Insert(31)
q1.Insert(2)
q1.Insert(16)
q1.Insert(17)
q1.Insert(21)
print(q1)
q1.Delete()
print(q1)
q1.Delete()
print(q1)