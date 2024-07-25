### Adjacency List Implementation of Graph 

# Q1. Write a class Graph to implement list representation of graph data structure.

class Graph():

# Q2. In class Graph, define __init__() method to initialise instance object variable vertex_count and a dict adj_list where key is vertex number and value is a list of adjacent vertices.

    def __init__(self,vc):
        self.vertex_count=vc 
        self.adj_list={v:[] for v in range(vc)}


# Q3. In class Graph, define add_edge() method add an edge in the graph with given vertices and weight. 

    def add_edge(self,v1,v2,weight):
        if 0<=v1<self.vertex_count and 0<=v2<self.vertex_count:
            self.adj_list[v1].append((v2,weight))
            self.adj_list[v2].append((v1,weight))
        else:
            print("Invalid vertex number")


# Q4. In class Graph, define remove_edge() method to remove an edge from the graph. 

    def remove_edge(self,v1,v2):
        if 0<=v1<self.vertex_count and 0<=v2<self.vertex_count:
            self.adj_list[v1]=[(vertx,weight) for vertx,weight in self.adj_list[v1] if vertx !=v2]
            self.adj_list[v2]=[(vertx,weight) for vertx,weight in self.adj_list[v2] if vertx !=v1]
        else:
            print("Invalid vertex number")


# Q5. In class Graph, define has_edge() method to check whether an edge exists or not for a given pair of vertices.

    def has_edge(self,v1,v2):
        if 0<=v1<self.vertex_count and 0<=v2<self.vertex_count:
            return any(vertex==v2 for vertex, x in self.adj_list[v1])
        else:
            return False


# Q6. In class Graph, define print_adj_list() method to print adjacency list of graph.
    def print_adj_list(self):
        for vertex,n in self.adj_list.items():
            print(vertex,":",self.adj_list[vertex])


vc=int(input("Enter no. of vertices in the adjacency matrix: "))
g=Graph(vc)
g.add_edge(0,1,5)
g.add_edge(0,2,4)
g.add_edge(0,3,1)
g.add_edge(1,2,6)
g.add_edge(2,3,2)

g.print_adj_list()
print()
g.remove_edge(0,2)
g.print_adj_list()