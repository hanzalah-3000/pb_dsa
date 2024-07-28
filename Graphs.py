from Queue import Queue

class Vertex:
    def __init__(self,val):
        self.val=val
        self.adj=[]
        self.visited= False

class Graph:
    def BFS(self,start):
        q1= Queue()
        temp=[]

        if start.visited==False:
            start.visited= True
            q1.enqueue(start)

        while not (q1.isEmpty()):
            elem= q1.dequeue()
            temp.append(elem.val)

            for each in elem.adj:
                if each.visited== False:
                    each.visited=True
                    q1.enqueue(each)
        
        return temp

    def DFS(self,start,trav): 
        start.visited= True
        trav.append(start.val)

        for each in start.adj:
            if each.visited==False:
                self.DFS(each,trav)
        
        return trav

v1= Vertex("A")
v2= Vertex("B")
v3= Vertex("C")
v4= Vertex("D")
v5= Vertex("E")

v1.adj.append(v2)
v1.adj.append(v3)

v2.adj.append(v1)
v2.adj.append(v4)

v3.adj.append(v1)
v3.adj.append(v4)
v3.adj.append(v5)

v4.adj.append(v2)
v4.adj.append(v3)
v4.adj.append(v5)

v5.adj.append(v3)
v5.adj.append(v4)

graph= Graph()
# print(graph.BFS(v1))
print(graph.DFS(v1,[]))
