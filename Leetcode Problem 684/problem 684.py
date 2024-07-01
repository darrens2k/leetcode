def findRedundantConnection(edges):

    # use the union-find algo

    # create lists for parents and ranks
    # parent stores the parent of each node
    # if 2 nodes have the same parent, they are connected
    # initially each node is a parent of itself
    parent = [x for x in range(len(edges))]
    # rank stores the size of the subgraph that each node is the parent of
    rank = [1 for x in range(len(edges))]

    # create a list to store redundant edges
    redundant = []

    # create the find and union functions for unionfind
    
    # This function will find the root of the subgraph node n is in
    def find(n):
        
        # if the parent[n] = n, then we have found the root
        if parent[n] != n:
            # if we're here we haven't found the root
            
            # path compression
            
            # when the recursive calls return this will update the parent of 
            # each node in the subgraph to be the root
            parent[n] = find(parent[n])
        
        # return the root
        return parent[n]
    
    # This will combine two subgraphs together
    def union(n1, n2):
        # get the roots of the subgraphs
        r1 = find(n1)
        r2 = find(n2)
        
        # if they have the same root, they are connected and we can't merge them
        if r1 == r2:
            return False
        else:
            # we can merge them
            
            # merge the higher rank (bigger size) graph into the smaller one
            if rank[r1] >= rank[r2]:
                # n1 becomes parent of n2
                parent[r2] = r1
                # n1 gains the rank of n2
                rank[r1] += rank[r2]
            else:
                # reverse of the above situation
                parent[r1] = r2
                rank[r2] += rank[r1]
            
            # if we reached here, we can union
            return True
    
    # iterate through the input edges
    for edge in edges:
        # grab the start and end nodes of the edge
        start, end = edge
        # decrement start and end for array indexing
        start = start - 1
        end = end - 1
        
        # attempt to union them
        if not union(start, end):
            # if here we cant union
            # add edge to list of redundant edges
            redundant.append(edge)
    # return the last redundant edge found
    return redundant[-1]
        

findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]])