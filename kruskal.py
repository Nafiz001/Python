import DisjointSet as dst

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
        self.nodes=[]
        self.MST=[]
    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])
    def addNode(self,value):
        self.nodes.append(value)
    def printSol(self,s,d,w):
        for s,d,w in self.MST:
            print("%s - %s: %s" % (s,d,w))
    def kruskal(self):
        i,e=0,0
        ds =dst.DisjointSet(self.nodes)
        self.graph=sorted(self.graph,key=lambda x:x[2])
        while e<self.V-1:
            s,d,w=self.graph[i]
            i+=1
            x=ds.find(s)
            y=ds.find(d)
            if x!=y:
                e+=1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printSol(s,d,w)
g=Graph(5)
g.addNode('A')
g.addNode('B')
g.addNode('C')
g.addNode('D')
g.addNode('E')
g.addEdge('A','B',5)
g.addEdge('A','C',13)
g.addEdge('A','E',15)
g.addEdge('B','C',10)
g.addEdge('B','D',8)
g.addEdge('C','D',6)
g.addEdge('E','C',20)
g.kruskal()
        
            