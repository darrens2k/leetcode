def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """

    # initialize loop counter
    i = 0

    # iterate through input string s, but only the first half
    while (i + 1) <= (len(s) / 2):

        # gap between current index and the index it should be swapped with would be len(s) - 1 - i (assuming i is the index of the current element)

        # grab current element
        current_elem = s[i]

        # grab the element it should be swapped with
        swap_elem = s[len(s) - 1 - i]

        # replace the elements with each other
        s[i] = swap_elem
        s[len(s) - 1 - i] = current_elem

        # increment loop counter
        i += 1
        
# test cases
s = ["H","a","n","n","a","h"]
reverseString(s)
print(s)
    