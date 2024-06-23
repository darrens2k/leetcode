def max_possible_K(binary_string):
    n = len(binary_string)
    count_of_1s = binary_string.count('1')
    
    def divisors(x):
        divs = []
        for i in range(1, x + 1):
            if x % i == 0:
                divs.append(i)
        return divs
    
    possible_Ks = divisors(count_of_1s)
    
    # Filter the possible Ks to be <= n
    possible_Ks = [k for k in possible_Ks if k <= n]
    
    # Return the maximum possible K
    return max(possible_Ks) if possible_Ks else 0

# Example usage:
binary_string = "101"
print(max_possible_K(binary_string))  # Output: 3
