from collections import defaultdict
import sys

class Graph:
    def __init__(self):
        self.dict=[]
        self.par=[]
        self.vert=[]
    def addEdge(self,u,v,w):
        self.dict.append([u,v,w])

    def parent(self,v):
        for i in range(v):
            self.par.append(i)
    def addVertices(self,a,b):
        self.vert.append([a,b])
    def kruskals(self,v):
        for i in range(v):
            min=sys.maxsize
            j=0
            while(j<(len(self.dict))):
                if min>self.dict[j][2] and self.par[self.dict[j][0]]!=self.par[self.dict[j][1]]:
                    min=self.dict[j][2]
                    index=j
                j+=1
            a=self.dict[index][0]
            b=self.dict[index][1]
            if self.par[a]>self.par[b]:
                self.par[a]=self.par[b]
            else:
                self.par[b]=self.par[a]
            self.addVertices(a,b)
            del(self.dict[index])
        print(self.vert)
g=Graph()
g.addEdge(0,1,1)
g.addEdge(0,2,1)
g.addEdge(1,2,1)
g.addEdge(2,3,2)
g.addEdge(3,0,2)
g.parent(4)
g.kruskals(3)
