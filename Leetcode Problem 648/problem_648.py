def replaceWords(dictionary, sentence):
        
    # split sentence into a list of words
    split_sent = sentence.split()

    # create output list
    output = []

    # iterate through the sentence
    for i in range(len(split_sent)):
        
        # grab current word
        word = split_sent[i]

        # create list to store roots that match the word
        roots = []

        # iterate through the possible roots and check if they occur in the word
        for root in dictionary:

            if root in word[:len(root)]:
                # check if the root appears at the start of the word
                # if root is in word, add to the list of possible roots
                roots.append(root)
        
        # if there is no possible root, add the word to the output as is
        if len(roots) == 0:
            output.append(word)

        # if there is 1 root, add that to the output
        elif len(roots) == 1:
            output.append(roots[0])

        # if there are multiple roots, select the shortest one
        else:
            # initialize shortest length
            shortest_len = 1000000
            # variable to store index of shortest root
            shortest_index = 0

            # iterate through all roots
            for i in range(len(roots)):
                if len(roots[i]) < shortest_len:
                    shortest_len = len(roots[i])
                    shortest_index = i
            
            # append shortest root to output
            output.append(roots[shortest_index])
    
    # iterate through output list and create an output string
    output_string = ""
    for i in range(len(output)):

        # add no space at the end if it is the last word
        if i == (len(output) - 1):
            output_string += output[i]
        # add space at the end otherwise
        else:
            output_string += output[i] + " "
    
    # return output
    return output_string

# Test solution
print(replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))

