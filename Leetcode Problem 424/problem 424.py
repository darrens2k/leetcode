def characterReplacement(s, k):

    # create a dictionary to keep a count of the characters that appear in the string
    counts = {'A':0, 'B':0, 'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,
            'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,
            'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    
    # Helper function to get the currently most popular character in a window
    def mostPopular():
        
        # most popular index and count
        count = -1
        popChar = -1
        
        # find the character with the highest count in the window
        for x in counts:
            if counts[x] > count:
                count = counts[x]
                popChar = x
        return count
    
    # window bounds
    start, end = 0, 0
    
    # max found so far
    maxCount = 0
    maxWindowLen = 0
    
    # iterate through input
    while end < len(s):
        
        # get current character and update its count
        char = s[end]
        counts[char] += 1
        
        # get count of most popular char in window
        maxCount = mostPopular()

        # check if window is too large
        windowLen = end - start + 1 
        print(char, windowLen, maxCount, start, end)
        if windowLen - maxCount <= k:
            # save the max valid window length
            if windowLen > maxWindowLen:
                maxWindowLen = windowLen
                print("max", windowLen)
            # our window can be grown
            end += 1
        else:
            # our window is too big, we cant make enough replacements
            # slide the window
            # lower the count of the character removed
            counts[s[start]] -= 1
            start += 1
            end += 1
            
        
    return maxWindowLen
    
characterReplacement('ABAA', 0)