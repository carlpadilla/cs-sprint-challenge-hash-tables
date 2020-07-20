def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    paired_numbers = {}

    for i in range(0, length):
        item = limit - weights[i]
        if item in paired_numbers:
            if i != paired_numbers[item]:
                return [i, paired_numbers[item]]
        paired_numbers[weights[i]] = i

    return None
