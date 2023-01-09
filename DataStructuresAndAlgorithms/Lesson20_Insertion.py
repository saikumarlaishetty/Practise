# Insertion of node

class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    # insertion
    def insert(self,data):
        if self.key is None:   # if tree is empty
            self.key = data
            return
        if self.key == data:   # if duplicate ignore
            return
        if self.key > data:    # if data is lower then lchild
            if self.lchild:
                self.lchild.insert(data)     # recursion function
            else:
                self.lchild = BST(data)
        else:                   # if data is higher the rchild
            if self.rchild:
                self.rchild.insert(data)      # recursion function
            else:
                self.rchild = BST(data)

    # Search
    def search(self,data):
        if self.key is None:
            print("Tree is empty")
            return
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree!")

    # Traversal 1) Pre order  2) In Order 3) Post order
    # 1) Pre order  = root---> lchild ---> rchild
    def preorder(self):
        print(self.key,end=" ")     # root key
        if self.lchild:
            self.lchild.preorder()          # recursion function
        if self.rchild:
            self.rchild.preorder()          # recursion function

    # 2) In order = lchild --> root --> rchild
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    # 3) post order  = lchild --> rchild --> root
    def postorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.rchild:
            self.rchild.inorder()
        print(self.key, end=" ")

    # 4) Deletion
    def delete(self,data,curr):
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key :   # check in left subtree
            if self.lchild:
                self.lchlild = self.lchlid.delete(data,curr)
            else:
                print("Given node is not present in tree")
        elif data > self.key :       # check in right sub tree
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("Given node is not present in tree")
        else:
            if self.lchild is None:  # 0 or 1 child nodes
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None: # 0 or 1 child nodes
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            # if there are 2 childs node for a parent node
            # replace smallest of right sub tree
            # replace largest of left sub tree
            node = self.rchild    # smallest node in right sub tree
            while node.lchild:    # smallest nodes will be present in lchild
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
            return self

    # Method to find min node
    def min_node(self):
        curr = self
        while curr.lchild:
            curr = curr.lchild
        print("Node with smallest key is ", curr.key)

    # Method to find max node
    def max_node(self):
        curr = self
        while curr.rchild:
            curr = curr.rchild
        print("Node with maximum key is ",curr.key)


def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)





root = BST(10)

list1 = [6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)

print("Pre Order")
root.preorder()
print()

root.min_node()
root.max_node()


#if count(root) > 1:
#    root.delete(10,root.key)
#else:
#    print("Can't perform deletion operation")

#root.delete()
#print("After deleting :")
#root.preorder()