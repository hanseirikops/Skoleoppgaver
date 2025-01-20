#Exercise 1 
#a) True
#b) False, (2,1) is not in the edge set 
#c) True (1,2),(2,3),(3,4),(4,1) is a cycle

#Exercise 2
class Graph: 
    graph = dict()

    def add_edge(self, node, neighbour): 
        if node not in self.graph: 
            self.graph[node] = [neighbour] 
        else: 
            self.graph[node].append(neighbour) 
    
    def print_graph(self): 
        print(self.graph)
    
    def nodes_out_degree(self, n):
        liste=[]
        for nodes, connectionin in self.graph.items():
            if len(connectionin)==n:
                liste.append(nodes)
        return liste
    
    #Excersise 3
    #a)
    def remove_edge(self, node1,node2):
        if node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
    
    #b)
    def bfs(self,start):
        visited=[start]
        queue=[start]
        while queue:
            vertex=queue.pop(0)
            for neighbour in self.graph.get(vertex,[]):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

graph = Graph() 
graph.add_edge('A', 'B') 
graph.add_edge('A', 'C') 
graph.add_edge('B', 'A') 
graph.add_edge('C', 'A') 
graph.add_edge('B', 'C') 
graph.add_edge('F', 'B')
graph.print_graph()
print(graph.nodes_out_degree(2))
graph.remove_edge('A','B')
graph.print_graph()
print(graph.bfs('B'))