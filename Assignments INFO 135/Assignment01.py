# 1
import math

def worst_case_binary_search(number):
    print(math.ceil(math.log2(number)))

# a
worst_case_binary_search(102400)
# b
worst_case_binary_search(480000)

# 2

class Node:
    def __init__(self, name):
        self.name=name
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def print_list(self):
        list1=[]
        node=self.head
        while node!=None:
            list1.append(node.name)
            node=node.next
        print(list1)

node1=Node('potato')
node2=Node('salad')
node3=Node('onion')

potatosalad=LinkedList()
potatosalad.head=node1
node1.next=node2
node2.next=node3

potatosalad.print_list()

# 3

class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items)==0:
            return None
        return self.items.pop()
    
def reverse_list(list1):
    temp=Stack()
    for i in list1:
        temp.push(i)
    rev=[]
    while len(temp.items)>0:
        rev.append(temp.pop())
    print(rev)

my_list=[1,2,3,4,5]

reverse_list(my_list)