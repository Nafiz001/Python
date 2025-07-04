# class Graph:
#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict={}
#         self.gdict= gdict
#     def addEdge(self,vertex,edge):
#         self.gdict[vertex].append(edge)
#     def bfs(self,start, end):
#         queue=[[start]]
#         while queue:
#             dever=queue.pop(0)
#             node=dever[-1]
#             if node==end:
#                 return dever
#             for ad in self.gdict.get(node,[]):
#                 new_path=list(dever)
#                 new_path.append(ad)
#                 queue.append(new_path)
#     def dfs(self,vertex):
#         vis=[vertex]
#         stack=[vertex]
#         while stack:
#             p=stack.pop()
#             print(p)
#             for ad in self.gdict[p]:
#                 if ad not in vis:
#                     vis.append(ad)
#                     stack.append(ad)
                
                    
# customDict= {'a': ['b','c'],
#              'b':['d','g'],
#              'c':['d','e'],
#              'd':['f'],
#              'e':['f'],
#              'g':['f']}
# graph= Graph(customDict)
# print(graph.bfs('a','f'))
# graph.dfs('a')
from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes=set()
        self.edges=defaultdict(list)
        self.distances={}
    def addNode(self,value):
        self.nodes.add(value)
    def addEdge(self,fromNode,toNode,distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode,toNode)]=distance
def dijkstra(graph,initial):
    vis={initial:0}
    path=defaultdict(list)
    nodes=set(graph.nodes)
    while nodes:
        minNode=None
        for node in nodes:
            if node in vis:
                if minNode is None:
                    minNode=node
                elif vis[node]<vis[minNode]:
                    minNode=node
        if minNode is None:
            break
        nodes.remove(minNode)
        curW=vis[minNode]
        for edge in graph.edges[minNode]:
            w=curW+graph.distances[(minNode,edge)]
            if edge not in vis or w<vis[edge]:
                vis[edge]=w
                path[edge].append(minNode)
    return vis,path
    # def topSortU(self,v,vis,stack):
    #     vis.append(v)
    #     for i in self.graph[v]:
    #         if i not in vis:
    #             self.topSortU(i,vis,stack)
    #     stack.insert(0,v)
    # def topSort(self):
    #     vis=[]
    #     stack=[]
    #     for k in list(self.graph):
    #         if k not in vis:
    #             self.topSortU(k,vis,stack)
    #     print(stack)
    
customGraph=Graph()
customGraph.addNode('A')
customGraph.addNode('B')
customGraph.addNode('C')
customGraph.addNode('D')
customGraph.addNode('E')
customGraph.addNode('F')
customGraph.addNode('G')
customGraph.addEdge('A','B',2)
customGraph.addEdge('A','C',5)
customGraph.addEdge('B','E',3)
customGraph.addEdge('E','G',9)
customGraph.addEdge('F','G',7)
customGraph.addEdge('B','C',6)
customGraph.addEdge('B','D',1)
customGraph.addEdge('D','E',4)
customGraph.addEdge('C','F',8)
print(dijkstra(customGraph,'A'))

# Floyd-Warshall Algorithm for All Pairs Shortest Path
INF = 9999

def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end=' ')
        print(" ")

def floydWarshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    printSolution(nV, distance)

# Test Floyd-Warshall
G = [[0, 8, INF, 1],
     [INF, 0, 1, INF],
     [4, INF, 0, INF],
     [INF, 2, 9, 1],
     ]
floydWarshall(4, G)
