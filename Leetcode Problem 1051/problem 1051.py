def heightChecker(heights):
        
        # counter for amount of incorrect indices
        counter = 0
        
        # create copy of the input list
        copy = [0 for i in range(len(heights))]
        for i in range(len(heights)):
            copy[i] = heights[i]

        # begin by sorting the array
        # use quick sort
        
        # create recursive function to create the new position of the pivot
        # input_list = the array to be worked on
        # pivot_index = position of the pivot element
        # start_index = starting index of the sub-list currently being worked on
        # end_index = ending index of the sub-list 
        def locate_pivot_index(input_list, start, end):

            # get value of the pivot (assume pivot is the last element in the list)
            pivot = input_list[end]
            
            # Strategy:
            #   Locate the first element from the left that is larger than the pivot
            #   Locate first element from the right that is smaller than the pivot
            #   Swap them
            #   Stop iterating when the index of the right element is smaller than the index of the right element
            
            # index of first item from the right that is smaller than pivot
            indexRight = end - 1
            
            # index of first item from left that is bigger than the pivot
            indexLeft = start

            # go through the list and check if each element is bigger or smaller than the pivot
            while indexRight >= indexLeft:
                
                # if the current left number is smaller than the pivot, move on
                if input_list[indexLeft] <= pivot:
                    indexLeft += 1
                # if the current right number is bigger than pivot, move on
                elif input_list[indexRight] >= pivot:
                    indexRight -= 1
                # if neither is the case, then the elements must be swapped
                else:
                    input_list[indexLeft], input_list[indexRight] = input_list[indexRight], input_list[indexLeft]
            
            # put the pivot between the left and right sections
            input_list[end], input_list[indexLeft] = input_list[indexLeft], input_list[end]
            
            return indexLeft
        
        # quicksort main function
        def quickSort(input_list, start, end):
            
            # if we have not sorted entire list
            if start < end:
                pivot_index = locate_pivot_index(input_list, start, end)
                # recurse on left side
                quickSort(input_list, start, pivot_index - 1)
                # recurse on right side
                quickSort(input_list, pivot_index + 1, end)
        
        # sort the input heights list
        quickSort(heights, 0, len(heights) - 1) 
        
        # iterate through the sorted list and input to locate mismatches
        for i in range(len(copy)):
            if copy[i] != heights[i]:
                counter += 1

        # # return total amount of indices that are out of place
        return counter
    
heightChecker([1,1,4,2,1,3])