#lab8
#Excercise 1
#a)
#tree
#b)
#complete binary tree
#c)
#perfect binary tree

#Excercise 2
class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None
    
    def insert_left(self, value):
        if self.left_child is None:
            self.left_child=BinaryTree(value)
        
        else: 
            new_node=BinaryTree(value)
            new_node.left_child=self.left_child
            self.left_child=new_node
    
    def insert_right(self, value):
        if self.right_child is None:
            self.right_child=BinaryTree(value)

        else:
            new_node=BinaryTree(value)
            new_node.right_child=self.right_child
            self.right_child=new_node

    def print_tree(self, level=0):
        print(' '*level*2+str(self.value))
        if self.left_child is not None:
            self.left_child.print_tree(level+1)
        if self.right_child is not None:
            self.right_child.print_tree(level+1)

tree=BinaryTree('A')
tree.insert_left('B')
tree.insert_right('C')
b_node=tree.left_child
b_node.insert_left('D')
b_node.insert_right('E')
tree.print_tree()

#Excercise 3
from hashlib import md5
def hackerman(door_id):
    pasword=''
    i=0
    while len(pasword)<4:
        string_value=door_id+str(i)
        encoded=string_value.encode()
        i+=1
        check=md5(encoded).hexdigest()
        if check[0]=='0' and check[1]=='0':
            pasword=pasword+check[3]
    print(pasword)

hackerman('abc')
hackerman('cyd')