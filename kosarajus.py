from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices
        self.rev_graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def reverseGraph(self):
        for i in self.graph:
            for j in self.graph[i]:
                self.rev_graph[j].append(i)
        print(self.rev_graph)
    def kosarajusort(self,v,visited,stack):
        visited[ord(v)%97]=True
        for i in self.graph[v]:
            if visited[ord(i)%97]==False:
                self.kosarajusort(i,visited,stack)
        stack=stack.append(v)
    def kosarajus(self):
        visited=[False]*self.V
        stack=[]
        
        for i in range(self.V):
            if chr(97+i) not in self.graph:
                self.graph[chr(97+i)]=[]
        for i in range(self.V):
            if visited[i]==False:
                self.kosarajusort(chr(97+i),visited,stack)
        print(stack)
        self.reverseGraph()
        self.after_reverse(stack)
    def rev_kosaraju(self,x,rev_visited):
        rev_visited[ord(x)%97]=True
        
        for p in self.rev_graph[x]:
            if rev_visited[ord(p)%97]==False:
                self.rev_kosaraju(p,rev_visited)
        print(x,end=" ")
    def after_reverse(self,stack):
        rev_visited=[False]*self.V
        final=[]
        for i in range(len(stack)):
            x=stack.pop()
            if rev_visited[ord(x)%97]==False:
                self.rev_kosaraju(x,rev_visited)
                print()
            
        
                
g=Graph(11)
for i in range(13):
    u,v=input().split()
    g.addEdge(u,v)
g.kosarajus()
