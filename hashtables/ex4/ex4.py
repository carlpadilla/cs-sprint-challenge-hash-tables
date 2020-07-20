def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Set up hash table

    cache = {}

    # result list
    result = []

    # Iterate through the numbers:
    for numbers in a:
        # Check for positive number
        if numbers > 0:
            # Check if positive numbers not in hash table
            if numbers not in cache:
                # Initialize entry with False
                cache[numbers] = False
            # Check if negative version is hash
            if -numbers in cache:
                cache[-numbers] = True
                cache[numbers] = True
        # Check for negative number
        else:
            # Check negative numb not in hash table
            if numbers not in cache:
                # Initialize entry with false
                cache[numbers] = False
            # Check for positive num is in hash table
            if abs(numbers) in cache:
                # Set value to true
                cache[abs(numbers)] = True
                cache[numbers] = True

    # Iterate the inputs
    for numbers, boolean in cache.items():
        if boolean is True and numbers > 0:
            result.append(numbers)
    print(numbers)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
