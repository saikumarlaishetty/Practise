# First node is head and last node is NULL


# A ) Add/Insertion 1) Begin 2) end 3) inbetween

# B) deletion of node 1) Begin 2) end 3) Inbetween

# C) Traversal : Start with head if the head is not NULL access the info
# Goto the next node access the info

# Implementation of single linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 3) Traversal
    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.ref

    # 1) Add beginning
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # 2) At the end
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # Between the nodes 1) after node 2) before the node\
    # 1) after node
    def add_after(self,data,x):
        n = self.head            # first node
        while n is not None:     # checking the condition whether its null
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # 2) before node
    def add_before(self,data,x):
        if self.head.data is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node is not found")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    # Linked list is empty
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    # Delete from start
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we can't delete nodes!")
        else:
            self.head = self.head.ref

    # Delete from last
    def delete_end(self):
        if self.head is None:
            print("LL is empty so we cant delete nodes!")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    # Delete from middle
    def delete_by_value(self,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        while self.head.ref is not None:
            if self.head.ref.data == x:
                self.head.ref = self.head.ref.ref
                break
            self.head = self.head.ref
        if self.head.ref is None:
            print("Node is not present")


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.delete_by_value(30)
#LL1.delete_begin()
#LL1.delete_end()
LL1.print_LL()



