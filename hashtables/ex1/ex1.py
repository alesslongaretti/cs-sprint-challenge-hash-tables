def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    pairs = {}
        
    #storing it to dictionary (storing values as keys in pairs, index loc as a value)
    for item in range(length):
        pairs[weights[item]] = item

    #looping to check if the result of limit - the value of weights exists in pairs
    for item in range(length):
        # if it does we return index of item being used (item ) and the index of the result
        if limit - weights[item] in pairs:
            # returning the higher values index first
            return (max(item, pairs[limit - weights[item]]), min(item, pairs[limit - weights[item]]))
    #if such pairs dont exist return none
    return None
    


