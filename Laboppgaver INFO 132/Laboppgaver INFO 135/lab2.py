#Linked list
#a)
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

#b)
node1=Node(1)
node2=Node(2)
node3=Node(3)
node1.next=node2
node2.next=node3

#c)
class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,new_data):
        new_node=Node(new_data)
        if self.head==None:
            self.head=new_node
        else:
            last_node=self.head
            while last_node.next!=None:
                last_node=last_node.next
            last_node.next=new_node
    
    #d)
    def add_at_beginning(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

tall=LinkedList()
tall.add(1)
tall.add(2)
tall.add(3)
tall.add_at_beginning('ERROR: IKKE ET TALL')

print(tall.head.data)
print(tall.head.next.data)
print(tall.head.next.next.data)
print(tall.head.next.next.next.data)