#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    
    for i in tickets:
        if i.source == 'NONE':
            route[0] = i.destination
        if i.destination == 'NONE':
            route[length-1] = i.source
        if i.source is not None and i.destination is not None:
            hash_table_insert(hashtable,i.source,i.destination)

    for index,g in enumerate(route):
        if g is None:
            route[index] = hash_table_retrieve(hashtable,route[(index-1)])
    route[length-1] = 'NONE'

    return route
