#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Set up tickets hash table
    table = {}
    # Set up route list
    route = [None] * length

    # Iterate through the tickets
    for ticket in tickets:
        # Set source as the key, and destination as the value.
        table[ticket.source] = ticket.destination

    route[0] = table["NONE"]
    route[1] = table[route[0]]

    # append to the route
    if length > 2:
        for i in range(2, length):
            route[i] = table[route[i-1]]

    # print(route)
    return route
