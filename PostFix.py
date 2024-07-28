class Stack:
    def __init__(self):
        self.top= -1
        self.array= []
    
    def checkEmpty(self):
        if len(self.array)==0:
            return True
        else:
            return False
    
    def push(self,item):
        self.array.append(item)
    
    def pop(self):
        if self.checkEmpty():
            return 'Stack is empty'
        return self.array.pop()
    
    def PostfixAnalysis(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                num1= self.pop()
                num2= self.pop()
                self.push(str(eval(num2+i+num1)))
        return int(self.pop())
exp = "231*+9-"

st1= Stack()
print(st1.PostfixAnalysis(exp))
print("Evaluation is %d"%st1.PostfixAnalysis(exp))