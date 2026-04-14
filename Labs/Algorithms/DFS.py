graph={
    'A':['B','C','D'],
    'B':[],
    'C':['E','F'],
    'E':[],
    'D':['F'],
    'F':[]
}

stack=[]
visited=[]

def DFS(startingNode,graph):
    #Step 01
    stack.append(startingNode)
    visited.append(startingNode)
    
    #Step 02
    while stack:
        node=stack.pop()
        print(node,end=" ")
        #step 03
        for child in graph[node]:  #B, C, D
            if child not in visited:
                stack.append(child)
                visited.append(child)


DFS('A',graph)

