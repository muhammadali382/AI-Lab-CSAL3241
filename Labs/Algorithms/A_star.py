graph={
    'S':{'A':3,'C':2,'D':2},
    'A':{},
    'B':{'E':2,},
    'C':{'F':1 },
    'D':{'B':3,'G':8,},
    'E':{'G':2},
    'F':{'E':0,'G':4,},
    'G':{},
}

Heuristic={
    'S':20,
    'A':18,
    'C':16,
    'D':14,
    'B':10,
    'E':9,
    'F':10,
    'G':0
}
def A_star(startingNode, goal,myGraph):
    cost=0
    path=[startingNode]
    
    visited =[]
    # queue=[3,'S-A',2,'S-C',2,'S-D']
    queue=[cost,path]
    #Even Index = Cost, Odd Index = Relevant PATH
    
    while queue:
        index=0
        minIndex=0
        #queue=[3,'[S,A]',2, '[S,D]']
        while index < len(queue):
            
            #Iter =1
            # queue[0] > queue[0]
            # 0 > 0
            
            
            #iter=2
            # queue[0] > queue[2]
            # 3>2
            
            # Iter =3
            # queue[2] > queue[4]
            # 2 > 2
             #queue=[3,'[S,A]',2, '[S,D]']
            currentNode = Heuristic[queue[minIndex+1][len(queue[minIndex+1])-1]]+queue[minIndex]
            nextNode = Heuristic[queue[index+1][len(queue[index+1])-1]]+queue[index]
            
            if currentNode > nextNode:
                minIndex=index
            index=index+2
            
        cost= queue.pop(minIndex) #2
        path = queue.pop(minIndex) #[S,C,E,F]
        last_visited=path[-1] #C
        
        if last_visited not in visited:
            visited.append(last_visited)
            
        if last_visited == goal:
            path.append(cost)
            return path
        
        
        for child in myGraph[last_visited].keys():#A, C, D
            newPath = list(path)  # [S]
            newPath.append(child) # [S,D]
            queue.append(cost+myGraph[last_visited][child])
            queue.append(newPath)
    
print(A_star('S','G',graph))
    
    


# if (queue[minIndex]> queue[index]):




