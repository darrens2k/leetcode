def maxNumEdgesToRemove(n, edges):
    
    # counter to store number of removed edges
        removed = 0

        # create adj matrix for bob abd alice
        bob = [[0 for i in range(n)] for j in range(n)]
        alice = [[0 for i in range(n)] for j in range(n)]
        # loop to fill in adj matrices
        for edge in edges:            
            # get info about edge
            edgeType, start, end = edge
            # if type 1, add to alice
            if edgeType == 1 and alice[start - 1][end - 1] == 0:
                alice[start - 1][end - 1] = 1
                alice[end - 1][start - 1] = 1
            elif edgeType == 2 and bob[start - 1][end - 1] == 0:
                bob[start - 1][end - 1] = 1
                bob[end - 1][start - 1] = 1
            else:
                # edge type must be 3    
                # if 2 nodes have a type 3 edge, any other edge between them can be dropped
                
                # check if an edge exists already
                if alice[start - 1][end - 1] == 1 and bob[start - 1][end - 1] == 1:
                    # edge already exists
                    removed += 1
                else:
                    # no edge exists yet
                    alice[start - 1][end - 1] = 1
                    alice[end - 1][start - 1] = 1
                    bob[start - 1][end - 1] = 1
                    bob[end - 1][start - 1] = 1
        # use dfs to check if there a path to every node from a random starting node
        # if a node is seen more than once in dfs, one of its edges can be dropped
        
        # create helper function to perform dfs on a graph
        def dfs(graph):
            
            # initialize stacks
            visited = []
            unvisited = [0]
            
            # counter to see how many times each node has popped up
            nodes = [0 for i in range(n)]
            
            # loop through graph
            while len(unvisited) > 0:
                
                # get current node
                currentNode = unvisited.pop(0)
                # mark current node as visited
                visited.append(currentNode)
                
                # get the neighbours of the current node
                neighbours = []
                for i in range(n):
                    if graph[currentNode][i] == 1:
                        neighbours.append(i)
                        # increment node counter
                        nodes[i] += 1
                        print(nodes, currentNode)
                # if a neighbour has not been visited yet, add them to unvisited
                for neighbour in neighbours:
                    if neighbour not in visited:
                        unvisited.append(neighbour)
            print(nodes)
            return nodes
        dfs(alice)
        print(bob)
        print(alice)
        return removed

# Test case
maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])