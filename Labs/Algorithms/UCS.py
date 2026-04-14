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

def UCS(startingNode, goal, mygraph):
    cost=0
    path=[startingNode] #['S']
    visited =[]
    queue=[cost,path]  #['S']
    #Even Index = cost , Odd Index = relevant Path
    currentNode=""
    
    while queue:
        index=0
        minIndex=0
        
        while index < len(queue):
            #queue[0] > queue[0]
            #0 > 0
            #queue[0] > queue[2]
            #3 > 2
            #queue[2] > queue[4]
            # 2 >2
            #queue=[3,'[S,A]','[S,C]',2,'[S,D]']
            if(queue[minIndex]> queue[index]):
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
    

print(UCS('S','G', graph))
    



