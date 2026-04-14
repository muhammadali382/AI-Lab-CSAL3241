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

Heuristics={  # Dummy Values but in Quesion, you have to analyze on your own.
    'S':20,
    'A':18,
    'C':16,
    'D':14,
    'B':10,
    'E':9,
    'F':10,
    'G':0
}
def GBFS(startingNode, goal, mygraph):
    cost=0
    path=[startingNode] #['S']
    visited =[]
    queue=[cost,path]  #[]
    #Even Index = cost , Odd Index = relevant Path
    
    while queue:
        index=2
        minIndex=0
        
        #queue=[3,'[S,A]','[S,C]',2,'[S,D]']
        
        while index < len(queue):
            
            
            currentNode= Heuristics[queue[minIndex+1][len(queue[minIndex+1])-1]]
            nextNode =Heuristics[queue[index+1][len(queue[index+1])-1]]
            if currentNode > nextNode:
                minIndex=index
            index=index+2
            
        cost = queue.pop(minIndex) # 2
        path = queue.pop(minIndex) #'[S,C]
        last_visited = path[-1] # C
        
        if last_visited not in visited:
            visited.append(last_visited)
            
        if last_visited == goal:
            path.append(cost)
            return path
        
        for child in mygraph[last_visited].keys():
            newPath = list(path) #[S]
            newPath.append(child) #[S,D]
            queue.append(cost+mygraph[last_visited][child])
            queue.append(newPath)
    

print(GBFS('S','G', graph))
    



