def has_negatives(a):
    # hash table
    pairs = {}
    # result array
    result = []

    for num in a:
        if -num in pairs:
            result.append(abs(num))
        else:
             pairs[num] = "value"

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
