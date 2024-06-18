def minOperations(nums):
        # counter for moves
        counter = 0
        
        # begin iterating through input
        for i in range(len(nums) - 1):

            # condition for strictly increasing
            if not(nums[i + 1] > nums[i]):
            
                # increase next element by their difference
                counter += nums[i] - nums[i + 1] + 1
                nums[i + 1] += nums[i] - nums[i + 1] + 1
                
        return counter
    
# test case
print(minOperations([1,5,2,4,1]))