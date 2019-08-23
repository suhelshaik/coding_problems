from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.V=v
        self.graph=defaultdict(list)
        self.black_set=[False]*self.V
        self.gray_set=[False]*self.V
        self.whiteset=[True]*self.V
        self.parent_map=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def cycle_dfs(self,v):
        self.gray_set[v]=True
        for j in self.graph[v]:
            if self.whiteset[j]==True:
                self.parent_map[j].append(v)
                self.whiteset[j]=False
                self.cycle_dfs(j)
            elif self.gray_set[j]==True and self.black_set[j]==False:
                x=v
                print(j,end=" ")
                try:
                    while(x is not None):
                        print(x,end=" ")
                        x=self.parent_map[x][-1]
                except:
                    print("cycle")

        self.black_set[v]=True
    def detect_cycle(self):
        print(self.graph)
        for i in range(self.V):
            if self.whiteset[i]==True:
                self.whiteset[i]=False
                self.parent_map[i]=None
                self.cycle_dfs(i)
                self.gray_set=[False]*self.V
                
g=Graph(5)
e=int(input())
for i in range(e):
    u,v=map(int,input().split())
    g.addEdge(u,v)
g.detect_cycle()
