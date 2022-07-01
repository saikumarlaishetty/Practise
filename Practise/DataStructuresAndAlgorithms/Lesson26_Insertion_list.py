# # Function to add a node using adjacency list representation

def add_node(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v] = []

# Function to add edge using adjacency list representation
"""
# undirected unweighted graph
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
"""

"""
# undirected weighted graph
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)
        
        """


"""
# directed weighted graph
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,cost]
        #list2 = [v1,cost]
        graph[v1].append(list1)
        #graph[v2].append(list2)
"""


# directed unweighted graph
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        #list1 = [v2,cost]
        #list2 = [v1,cost]
        graph[v1].append(v2)
        #graph[v2].append(list2)


# deletion
# 1) node
# 2) edge

# delete node(v)
# Adj Matrix
# Delete the row and column of index v

# Adj list
# Delete key and value pair of v and check the value of all key in
# dictionary for v , if it is present remove that from the list

"""
# directed weighted graph
# undirected and unweighted graph
def delete_node(v):
    if v not in graph:
        print(v, " is not present in graph")
    else:
        graph.pop(v)  # delete v from dict
        for i in graph:
            if v in graph[i]:
                graph[i].remove(v)
"""

# directed and weighted graph
def delete_node(v):
    if v not in graph:
        print(v, " is not present in graph")
    else:
        graph.pop(v)  # delete v from dict
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break


# delete edge
"""
# unweighted undirected graph
def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in graph")
    elif v2 not in graph:
        print(v2,"is not present in graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
"""

"""
# unweighted directed graph
def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in graph")
    elif v2 not in graph:
        print(v2,"is not present in graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            #graph[v2].remove(v1)
            """


# weighted undirected graph
def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"is not present in graph")
    elif v2 not in graph:
        print(v2,"is not present in graph")
    else:
        temp1 = [v1,cost]
        temp2 = [v2,cost]
        if temp2 in graph[v1]:
            graph[v1].remove(temp2)
            graph[v2].remove(temp1)


# Graph traversal algorithm
# 1) DFS : Depth first search
#       - Consider starting node as current node and visit that node.
#       - visit the unvisited adjacent node of current node, make that node as a current node
#       - Follow step 2 until we reach dead end
#       - If unvisited nodes are present in the graph then back track
#       take recent visited node as current node repeat step 2
#

# stack algorithm used in DFS algorithm
# as DFS used LIFO model then we are using stack operations


"""
# Adjacency list representation
# recursion approach
# unweighted graph
def DFS(node,visited,graph):   # node = starting node
    '
    DFS recursion approach for traversal
    :param node: starting node
    :param visited:
    :param graph:
    :return:
    '
    if node not in graph:
        print(node,"is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
"""

# Adjacency list representation
# recursion approach
# weighted graph
def DFS(node,visited,graph):   # node = starting node
    """
    DFS recursion approach for traversal
    :param node: starting node
    :param visited:
    :param graph:
    :return:
    """
    if node not in graph:
        print(node,"is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)


# Implement DFS algorithm
# using Iterative approach
def DFSiterative(node,graph):
    visited = set()
    if node not in graph:
        print(node, "is not present in the graph")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)






#visited = set()  # as we are using recursive approach the function is called again and again so we have take variable
                 # outside the function
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")

print(graph)
#DFS("K",visited,graph)
DFSiterative("A",graph)