import sys
class Graph:
    def __init__(self,v):
        self.graph=[]
        self.distance=[sys.maxsize]*v
        self.parent=[-1]*v
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def bellman_ford(self,v):
        self.distance[0]=0
        for i in range(v-1):
            for j in self.graph:
                if self.distance[j[1]]>self.distance[j[0]]+j[-1]:
                    self.distance[j[1]]=self.distance[j[0]]+j[-1]
                    self.parent[j[1]]=j[0]
        print(self.parent)
    def find_path(self,u,v):
        final=[]
        while(u!=v):
            final.append(v)
            v=self.parent[v]
        final.append(u)
        print(final)
        
g=Graph(5)
g.addEdge(3,4,2)
g.addEdge(4,3,1)
g.addEdge(2,4,4)
g.addEdge(0,2,5)
g.addEdge(1,2,-3)
g.addEdge(0,3,8)
g.addEdge(0,1,4)
g.bellman_ford(5)
g.find_path(1,4)
g.find_path(0,4)
g.find_path(0,3)
