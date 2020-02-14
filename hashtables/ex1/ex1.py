#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):

    ht = HashTable(16)
    #Insert weights:index kv pairs
    for i in range(0, length):
    	hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
    	cur_weight = weights[i]
    	answer = hash_table_retrieve(ht, limit-cur_weight)
    	#If answer is found
    	if answer:

    		if i > answer:
    			return (i, answer)
    		else:
    			return (answer, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")