# Binary search tree or ordered search tree

# Binary search tree is a binary tree with following properties:
# 1) The left subtree of a node contains only nodes with keys lesser than nodes key
# 2) The right subtree of a node contains only nodes with keys greater than nodes key
# 3) The left subtree and right subtree each must also be a BST


# How to deal with duplicates with BST ?
# there are 3 below ways as per different books:
# duplicate values are not allowed
#    or
# if duplicate values are present it should be left side
#    or
# if duplicate values are presenet it should be right side
#   or
# we can keep the counter for the duplicate values as below
# for 3 2 5 3  values
#     3(2)
#   2(1)   5(1)