# Adjacency Matrix Implementation of Graph 

# Q1. Write a class Graph to implement adjacency matrix representation of simple and undirectes graph. 

class Graph:

# Q2. In class Graph, define __init__() method to initialise vertex_count and adj_matrix (list of lists)

    def __init__(self,vc):
        self.vertex_count=vc
        self.adj_matrix=[[0]*vc for e in range(vc)]


# Q3. In class Graph, define add_edge() method add an edge in the graph with given weight. 

    def add_edge(self,v1,v2,weight):
        if v1>=0 and v1<self.vertex_count or v2>=0 and v2<=self.vertex_count:
            self.adj_matrix[v1][v2]=weight 
            self.adj_matrix[v2][v1]=weight
        else:
            print("Invalid vertex number")

# Q4. In class Graph, define remove_edge() method to remove an edge from the graph. 

    def remove_edge(self,v1,v2):
        if v1>=0 and v1<self.vertex_count or v2>=0 and v2<=self.vertex_count:
            self.adj_matrix[v1][v2]=0
            self.adj_matrix[v2][v1]=0
        else:
            print("Invalid vertex number")


# Q5. In class Graph, define has_edge() method to check whether two given vertices are connected by an edge or not.

    def has_edge(self,v1,v2):
        if v1>=0 and v1<self.vertex_count or v2>=0 and v2<self.vertex_count:
            print("Invalid vertex")
        else: 
            if self.adj_matrix[v1][v2]==0:
                return False
            else:
                return True


# Q6. In class Graph, define print_adj_matrix() method to print adjacency matrix.

    def print_adj_matrix(self):
        for i in (self.adj_matrix):
            print(" ".join(map(str,i)))


vc=int(input("Enter no. of vertices in the adjacency matrix: "))
g=Graph(vc)
g.add_edge(0,1,5)
g.add_edge(0,2,4)
g.add_edge(0,3,1)
g.add_edge(1,0,5)
g.add_edge(1,2,6)
g.add_edge(2,0,4)
g.add_edge(2,1,6)
g.add_edge(2,3,2)
g.add_edge(3,0,1)
g.add_edge(3,2,2)
g.print_adj_matrix()
print()
g.remove_edge(0,2)
g.remove_edge(2,0)
g.print_adj_matrix()