#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for index,i in enumerate(weights):
        hash_table_insert(ht,i,index)
    
    g = None
    i = -1
    while g is None and i < len(weights)-1:
        i += 1
        g = hash_table_retrieve(ht,limit-weights[i])
        
    if g is None:
        return None
    if g > i:
        return (g,i)
    else:
        return (i,g)
    


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
