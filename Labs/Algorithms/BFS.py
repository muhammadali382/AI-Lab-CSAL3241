graph={
    'A':['B','C','D'],
    'B':[],
    'C':['E','F'],
    'E':[],
    'D':['F'],
    'F':[]
}

queue=[]
visited=[]

def BFS(startingNode,graph):
    #Step 01
    queue.append(startingNode)
    visited.append(startingNode)
    
    #Step 02
    while queue:
        node=queue.pop(0)
        print(node,end=" ")
        #step 03
        for child in graph[node]:  #B, C, D
            if child not in visited:
                queue.append(child)
                visited.append(child)


BFS('A',graph)

