""" Here I use Brute force method.
    Brute force method is a way of solving problems by trying every possibility rather
    than using advanced techniques to improve efficiency.
    The downside of brute force method is the computing of shortest common
    superstring for every permutation. As the input grows, this will be exponentially
    large and takes forever to run.
"""

import itertools
from helper_fun import overlap, remove_duplicate_substring

def shortest_common_string(string_array):
    """ Return shortest common string.
        It checks all the possible combinations of reads.
    """
    read_list = remove_duplicate_substring(string_array)
    shortest_super_str = None
    for ssperm  in itertools.permutations(read_list):
        super_str = ssperm[0]
        for i in range(len(read_list)-1):
            overlap_len = overlap(ssperm[i], ssperm[i+1], min_length=1)
            temp_str = ssperm[i+1][overlap_len:]
            super_str += ssperm[i+1][overlap_len:]
        if (shortest_super_str is None) or (len(super_str) < len(shortest_super_str)):
            shortest_super_str = super_str
    return shortest_super_str