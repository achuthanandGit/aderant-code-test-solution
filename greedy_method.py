""" Here in this case I am using Greedy algorithm.
    The name greedy is because the algorith takes a series of decisions,
    and at each decision stage, ultimately chooses the option that shortens the 
    length of the superstring. It does not necessarily mean it will give the 
    optimal solution.
    While using Greedy algorithm, in each round, I will pick the longest overlap.
    The longer the overlap between the strings, the shorter the final string.

    Greedy algorithm works faster than brute force method. But sometimes this speed
    calculation may return a supersting, that contains all the input strings but not
    necessarily the shorted common superstring. But provides better performance than 
    brute force.
"""
import itertools
from helper_fun import pick_maximal_overlap, remove_duplicate_substring

def greedy_shortest_common_string(reads):
    """ Return shortest common string utilizing the maximum overlap length
    """
    read_list = remove_duplicate_substring(reads)
    # Calculating the two reads and best overlap
    read_a, read_b, overlap_len = pick_maximal_overlap(read_list)
    
    while overlap_len > 0 :
        # Removing the pairs from original read
        read_list.remove(read_a)
        read_list.remove(read_b)
        # Appending the combination of read_a and read_b to the original read 
        read_list.append(read_a + read_b[overlap_len:])
        read_a, read_b, overlap_len = pick_maximal_overlap(read_list)
    return ''.join(reads)