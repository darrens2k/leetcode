def maxNumEdgesToRemove(n, edges):
    
    # counter to store number of removed edges
    removed = 0
    
    # set up arrays for UnionFind (1 instance bob, 1 instance alice)
    parentAlice = [x for x in range(n)]
    rankAlice = [1 for x in range(n)]
    parentBob = [x for x in range(n)]
    rankBob = [1 for x in range(n)]
    
    # set up functions for union find
    
    # find function to locate the root parent of a node
    def find(n, parent):
        # if the node is parent of itself, it is the root
        if parent[n] != n:
            # path compression
            # update parent of each node in subgraph to be the root
            parent[n] = find(parent[n], parent)
        # return root
        return parent[n]
    
    # union function to merge two subgraphs
    def union(node1, node2, parent, rank):
        # get the roots of each node
        r1 = find(node1, parent)
        r2 = find(node2, parent)
        
        # if roots are the same, nodes are already connected
        if r1 == r2:
            return False
        else:
            # nodes are not connected yet
            
            # merge larger (higher rank) subgraph into the other
            if rank[r1] >= rank[r2]:
                # r1 becomes parent of r2
                parent[r2] = r1
                # r1 gains rank of r2
                rank[r1] += rank[r2]
            else:
                # reverse of above scenario
                parent[r1] = r2
                rank[r2] += rank[r1]            
            # return True, we were able to union nodes
            return True
    
    # handle type 3 edges first
    # these can benefit both graphs
    for edge in edges:
        # get info about edge
        edgeType, start, end = edge
        # decrement nodes for array indexing
        start -= 1
        end -= 1
        if edgeType == 3:
            # try to union with alice
            if not union(start, end, parentAlice, rankAlice):
                # union failed, increment edges that can be removed
                removed += 1
            else:
                # union for alice was successful
                # try union for Bob
                union(start, end, parentBob, rankBob)
                # dont increment removed if bob fails, alice used the edge    
    
    # iterate through edges of type 1 and 2
    for edge in edges:            
        # get info about edge
        edgeType, start, end = edge
        # decrement nodes for array indexing
        start -= 1
        end -= 1
        
        # if edge is type 1, work on alice unionfind
        if edgeType == 1:
            # try to union with alice
            if not union(start, end, parentAlice, rankAlice):
                # union failed, increment edges that can be removed
                removed += 1
        # if edge is type 2, work on bob
        elif edgeType == 2:
            # try to union with bob
            if not union(start, end, parentBob, rankBob):
                # union failed, increment edges to be removed
                removed += 1

    # need to check if the graphs of bob and alice are connected
    # parent of each node in the graph should be the same
    # build a helper function to check this
    def checkConnected(parent):
        # get the root of the graph (arbitrarily select first node)
        root = find(0, parent)
        # check if every other node has the same root
        for i in range(1, len(parent)):
            if find(i, parent) != root:
                # graph is not connected if they do not share same root
                return False
        # if we made it here, the graph is connected
        return True
        
    # check if alice and bob graphs are connected
    if not checkConnected(parentAlice) or not checkConnected(parentBob):
        return -1 
    else:
        # if we make it here, there are edges to removed
        # return the sum of edges that can be taken from each of them
        return removed

# Test case
maxNumEdgesToRemove(4, [[3,2,3],[1,1,2],[2,3,4]])