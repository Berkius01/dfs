from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
  
    def isCyclicUtil(self, v, visited, recStack):

        visited[v] = True
        recStack[v] = True
        
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
  
       
        recStack[v] = False
        return False
  
   
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False

    def DFSUtil(self, v, visited):
  
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
  
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)


    def DFS(self, v):
  
        visited = set()
        self.DFSUtil(v, visited)
  
g = Graph(7)
print("calışiy")
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4,5)
g.addEdge(5,0)
g.addEdge(5,6)
g.DFS(3)
if g.isCyclic() == 1:
    print ("\nGraph has a cycle")
else:
    print ("Graph has no cycle")
edges = [(0,1), (0,2), (1,2), (2, 1), (2, 3), (3, 4), (4,5), (5,0), (5,6)]
G = nx.Graph()
G.add_edges_from(edges)
nx.draw_networkx(G)
plt.show()
