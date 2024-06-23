def solution(N, graph):
    
    # use input to create an adjacency matrix for the graph
    adjMatrix = []
    for i in range(N):
        adjMatrix.append([0 for x in range(N)])
    # iterate through input and fill in values
    for coords in graph:
        index1 = coords[0] - 1
        index2 = coords[1] - 1
        weight = coords[2]
        adjMatrix[index1][index2] = weight
        adjMatrix[index2][index1] = weight
    
    # compute distance from each city to every other city to fill in adj matrix    
    # perform DFS
    
    # initialize DFS
    visited = []
    unvisited = [0]
    
    # helper function update distances
    def updateDist(source, seen):
        dist = 0
        counter = len(visited) - 1
        dest = visited[-1]
        while counter > 1:           
            
            if adjMatrix[source][visited[counter]] != 0:
                adjMatrix[source][dest] += dist + adjMatrix[source][visited[counter]]
                break
            dist += adjMatrix[visited[counter - 1]][visited[counter]]
            counter -= 1
    
    # dfs loop
    while unvisited:
        
        node = unvisited.pop()
        neighbours = []
        # get neighbours of current node
        for j in range(N):
            if adjMatrix[node][j] != 0:
                neighbours.append(j)
        visited.append(node)
        if adjMatrix[0][visited[-1]] == 0:
            updateDist(0, visited)
        # if the neighbours are from cities that we have yet to visit, add them to univisited
        for neighbour in neighbours:
            
            if neighbour not in visited:
                unvisited.append(neighbour)
        
        
        
        
        print(visited, adjMatrix)
    
    return



solution(5, [[1, 2, 1],[2, 3, 2],[2, 4, 3],[1, 5, 4]])