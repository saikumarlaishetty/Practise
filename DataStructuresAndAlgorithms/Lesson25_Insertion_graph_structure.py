# Graph operations
# 1) Insertion
# 2) deletion
# 3) Traversal

# Insertion =
# a) add node/add vertex
# b) add edge


# Insertion
# Function to add node using adjacency matrix representation
def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present in the graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=" ")
        print()


# Function to add edge using adjacency matrix representation
"""
# undirected and unweighted graph
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1
"""

"""
# weighted graph
def add_edge(v1,v2, cost):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost

"""


# directed weighted graph
def add_edge(v1,v2, cost):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        #graph[index2][index1] = cost



"""
# directed unweighted  graph
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        #graph[index2][index1] = 1

"""

# Deletion of node
# function to delete a node using adjacency matrix representation
def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not present in the graph")
    else:
        index1 = nodes.index(v)
        node_count =  node_count - 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

# Function to delete an edge using adjacency matrix representation

"""
# undirected (weighted/unweighted)
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in graph")
    elif v2 not in nodes:
        print(v2,"is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0
"""

# directed (weighted/unweighted)
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in graph")
    elif v2 not in nodes:
        print(v2,"is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        #graph[index2][index1] = 0

nodes = []
graph = []
node_count = 0
print("Before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",5)
print("Graph after deleting: ")
delete_edge("A","C")
print("Graph after deleting: ")
print_graph()
print("Before adding nodes")
print(nodes)
print(graph)
print_graph()