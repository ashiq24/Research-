# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
 
from collections import defaultdict
 
#Class to represent a graph
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary 
                                # to store graph
        self.total_weights = 0
         
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        #print('parent: ', parent[i], ' ', i)
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])

        return parent[i]

        '''
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
        '''
        
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root 
        # and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

 

    # The main function to construct MST using Kruskal's 
        # algorithm
    def KruskalMST(self):
 
        result =[] #This will store the resultant MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]
 
            # Step 1:  Sort all the edges in non-decreasing 
                # order of their
                # weight.  If we are not allowed to change the 
                # given graph, we can create a copy of graph
        self.graph =  sorted(self.graph,key=lambda item: item[2])
 
        parent = [] ; rank = []
        parent.append(-1)
        rank.append(-1)
 
        # Create V subsets with single elements
        for node in range(self.V):
            aa = node + 1
            parent.append(aa)
            rank.append(0)
     
        # Number of edges to be taken is equal to V-1
        while e < self.V -1 :
 
            # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge does't cause cycle, 
                        # include it in result and increment the index
                        # of result for next edge
            if x != y:
                e = e + 1    
                result.append([u,v,w])
                self.union(parent, rank, x, y)            
            # Else discard the edge
 
        # print the contents of result[] to display the built MST
        print ("Following are the edges in the constructed MST")

        for u, v, weight in result:
            #print str(u) + " -- " + str(v) + " == " + str(weight)
            print ("%d --> %d == %d" % (u,v,weight))
            self.total_weights += weight
 




# Driver code
edges = input('Enter number of vertices: ')
g = Graph(int(edges))

turns = input('Enter number of edges: ')
turns =  int(turns)

for turn in range(turns):
    u = input('Enter u, v, w: ')
    v = input()
    w = input()
    u = int(u)
    v = int(v)
    w = int(w)
    print('################################################')
    g.addEdge(u,v,w)    



g.KruskalMST()

print('total cost: ', g.total_weights)

'''
g.addEdge(1,2,1)
g.addEdge(2,1,7)
g.addEdge(2,4,5)
g.addEdge(2,3,4)
g.addEdge(3,1,8)
g.addEdge(3,4,6)
g.addEdge(3,2,10)
g.addEdge(1,4,3)
g.addEdge(1,3,2)
g.addEdge(4,1,9)
g.addEdge(4,2,11)
g.addEdge(4,3,12)
'''

'''
g.addEdge(1,2,6)
g.addEdge(1,4,4)
g.addEdge(2,4,3)
g.addEdge(3,1,1)
g.addEdge(3,2,2)
g.addEdge(4,3,5)
'''
'''
g.addEdge(1-1,2-1,6)
g.addEdge(1-1,4-1,4)
g.addEdge(2-1,4-1,3)
g.addEdge(3-1,1-1,1)
g.addEdge(3-1,2-1,2)
g.addEdge(4-1,3-1,5)
'''


#g.KruskalMST()
 





















