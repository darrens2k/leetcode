def solution(arr, p, q, r):
    
    # variable to store the sum
    totSum = 0
    
    # build a helper function to find the minimum sum subarray of size n
    def minSum(inputArr, subSize):
        
        # use a queue keep track of the k elements, like a sliding window
        currentElems = []
        
        # variable to store the current sum
        tempSum = sum(currentElems)
        
        # variable to store sum so far
        ultSum = 1000000000
        
        # iterate through array
        for i in range(len(inputArr)):
            
            # if the window does not contain too many elements, add another
            if len(currentElems) < subSize:
                currentElems.append(inputArr[i])
            else:
                # we have k elems in the queue
                # compute its sum
                tempSum = sum(currentElems)
                # check if this sum is less than the min sum so far
                if tempSum < ultSum:
                    ultSum = tempSum
                    # save elements that led to the lowest sum
                    bestElems = [x for x in currentElems]
                # remove first added element from the queue and update sum
                tempSum -= currentElems.pop(0)
                # add the next element to the queue
                currentElems.append(inputArr[i])
                # check this sum now against min
                tempSum = sum(currentElems)
                if tempSum < ultSum:
                    ultSum = tempSum
                    # save elements that led to the lowest sum
                    bestElems = [x for x in currentElems]
        return ultSum, bestElems
    
    
        
    # compute the lowest sum of subarray with length 2
    val2, elems2 = minSum(arr, 2)
    # remove these elements from the array
    for elem in elems2:
        arr.remove(elem)
    
    # compute the lowest sum of subarray with length 3
    val3, elems3 = minSum(arr, 3)
    # remove these elements from the array
    for elem in elems3:
        arr.remove(elem)
    
    # compute the lowest sum of subarray with length 1
    val1, elems1 = minSum(arr, 1)
    # remove these elements from the array
    for elem in elems1:
        arr.remove(elem)
        
    print(val3, elems3)
    print(val2, elems2)
    print(val1, elems1)
    
    totSum = val1 + val2 + val3
    print(totSum)
    
    return totSum
                    
                
                
                    
                
        
    
    
    
print(solution([3, 1, 0, 5, 1, 6, 5, -1, -100], 1, 1, 1))