# Double linked list
# It has "Prev link" + "Data" + "next link"
# starting node is head and last node is tail
# 1) Insertion 2)Deletion 3)Traversal
# 1) Insertion a)begin b)end c)middle
# 2) Deletion a)begin b)end c)by value
# 3) Traversal a) Forward  b)backward
# Extra memory is needed in double linked list ( this is disadvantage)


class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None


class doublyLL:
    def __init__(self):
        self.head = None

    # Forward traversal
    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref

    # Backward traversal
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.pref

    # Insert the node when linked list is empty
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        print("Linked list is not empty")

    # Insert the node at begin
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # Insert the node at end
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    # add after the node
    def add_after(self,data,x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:  # at last node
                    n.nref.pref = new_node
                n.nref = new_node

    # add before the node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:  # before the first node
                    n.pref.nref = new_node
                n.pref = new_node

    #deletion 1)Begin 2)end 3)Value
    # delete begin
    def delete_begin(self):
        if self.head is None:
            print("DLL is empty can't delete")
        elif self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node")
        else:
            self.head = self.head.nref
            self.head.pref = None

    # Delete end
    def delete_end(self):
        if self.head is None:
            print("DLL is empty can't delete")
        elif self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    # delete by value
    def delete_by_value(self,x):
        if self.head is None:   # DLL is empty
            print("DLL is empty can't delete")
            return
        if self.head.nref is None:   # one node
            if self.head.data == x:
                self.head = None
            else:
                print("x is not present in DLL")
            return
        if self.head.data == x:       # First node
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:      # Middle nodes
            if n.data == x:
                break
            n = n.nref

        if n.nref is not None:       # Middle nodes
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:                         # Last nodes
            if n.data == x:
                n.pref.nref = None
            else:
                print("x is not present in DLL")


dl1 = doublyLL()
dl1.add_begin(10)
#dl1.add_begin(120)
#dl1.add_begin(220)
dl1.delete_by_value(10)
#dl1.delete_begin()
#dl1.delete_end()
dl1.print_LL()
#dl1.print_LL_reverse()







