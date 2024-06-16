def reverseParentheses(s):

    # stack to store indices
    indices = []
    
    # helper function to reverse the string between given indices
    def reverseString(string, start, end):
        
        # isolate section of string to be replaced    
        out = string[start + 1:end]
        
        # reverse this section
        out = out[::-1]
        
        newString = string[:start + 1] + out + string[end:]
        
        return newString
    
    # iterate through the input string
    for i in range(len(s)):
        
        # if we hit a '(', add the index to our stack
        if s[i] == '(':
            indices.append(i)
        
        # if we hit a ')', pop the latest index
        if s[i] == ')':
            
            # call helper function to reverse string between ()
            s = reverseString(s, indices.pop(), i)
    
    # create output string
    out = ""
    
    # iterate through string and remove all parantheses
    for i in range(len(s)):
        
        if s[i] != '(' and s[i] != ')':
            out += s[i]
            
    return out

# test case
reverseParentheses("(u(love)i)")