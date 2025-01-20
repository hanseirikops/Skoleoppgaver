#Exercise 1
#a) pre-order
#H,A,D,E,C,B,G,F
#b) in-order
#D,A,E,H,G,B,F,C
#c) post-order
#D,E,A,G,F,B,C,H

#Exercise 2
class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None
    
    def insert_left(self,value):
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
    
    def search(self, value):
        if self.value==value:
            return True
        if self.left_child and self.left_child.search(value):
            return True
        if self.right_child and self.right_child.search(value):
            return True
        return False
    
    def print_tree(self, level=0):
        print(' '*level*2+str(self.value))
        if self.left_child is not None:
            self.left_child.print_tree(level+1)
        if self.right_child is not None:
            self.right_child.print_tree(level+1)

def build_my_tree(liste):
    tree=BinaryTree(liste[0])
    if len(liste)>1:
        tree.left_child=build_my_tree(liste[1])
    if len(liste)>2:
        tree.right_child=build_my_tree(liste[2])
    return tree

my_list=['H',['A',['D','E']],['C',['B',['G','F']]]]

mye_tree=build_my_tree(my_list)
mye_tree.print_tree()

#Exercise 3
class BinarySearchTree:
    def __init__(self, value=None):
        self.value=value
        if self.value is not None:
            self.left_child=BinarySearchTree()
            self.right_child=BinarySearchTree()
        else:
            self.left_child=None
            self.right_child=None