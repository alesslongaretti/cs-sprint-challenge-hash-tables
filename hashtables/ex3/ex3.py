def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # results
    result = []
    #dict to hold key value pairs
    pairs = {}
    #loop through the each list in arrays
    for array in arrays:
        #loop through each item in each list
        for item in array:
            #if the item is in the dictionary(pairs)
            if item in pairs:
                # increase the key of the value by 1
                pairs[item] += 1 
            else:
                # else add the item with a value of 1
                pairs[item] = 1
                
    # loop through the the dictionary
    for i in pairs:
        #if the the value of the items in pairs == the length of the arrays
        #(meaning it exists in all of them)
        if pairs[i] == len(arrays):
            # add the keys to the result array
            result.append(i)

    return result




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
