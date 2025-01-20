#1
#All of the binary threes are full since all of the nodes have either zero or two children

#2
#Matrix (ii) correctly displays the adjacency matrix of the graph

#3
#The funcions binary_tree, get_left_child, get_right_child, insert_left_child, and insert_right_child are from the lecture notes.
def binary_tree(r):
    return [r,[],[]]

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left_child(root,new_branch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[new_branch,t,[]])
    else:
        root.insert(1,[new_branch,[],[]])

def insert_right_child(root,new_branch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[new_branch,[],t])
    else:
        root.insert(2,[new_branch,[],[]])

def make_tree():
    tree=binary_tree(1)
    insert_left_child(tree,2)
    insert_left_child(get_left_child(tree),4)
    insert_right_child(tree,3)
    insert_left_child(get_right_child(tree),5)
    insert_right_child(get_right_child(tree),6)
    print(tree)

make_tree()

#4
#a)
#The class Graph, and all contained within is from the lecture notes with some modefication to add_edge.
class Graph:
    def __init__(self):
        self.graph={}
    
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    
    def add_edge(self, from_vertex, to_vertex):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)

def build_my_graph2():
    my_graph=Graph()
    my_graph.add_edge('a','c')
    my_graph.add_edge('a','d')
    my_graph.add_edge('b','a')
    my_graph.add_edge('c','b')
    my_graph.add_edge('d','e')
    my_graph.add_edge('e','a')
    print(my_graph.graph)

build_my_graph2()

#5
#The class BinarySearchTree with the methods __init__, is_empty and insert is from the lecture notes

class BinarySearchTree:
    def __init__(self, value=None):
        self.value=value
        if self.value is not None:
            self.left_child=BinarySearchTree()
            self.right_child=BinarySearchTree()
        else:
            self.left_child=None
            self.right_child=None
    
    def is_empty(self):
        return self.value is None
    
    def insert(self,value):
        if self.is_empty():
            self.value=value
            self.left_child=BinarySearchTree()
            self.right_child=BinarySearchTree()
        elif value<self.value:
            self.left_child.insert(value)
        elif value>self.value:
            self.right_child.insert(value)
    
    def compute_sum(self):
        if self.is_empty():
            return 0
        return self.value+self.left_child.compute_sum()+self.right_child.compute_sum()

    def comput_count(self):
        if self.is_empty():
            return 0
        return 1 + self.left_child.comput_count()+self.right_child.comput_count()

my_tree=BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)
my_tree.insert(12)

print('sum:', my_tree.compute_sum())
print('number of nodes:', my_tree.comput_count())   