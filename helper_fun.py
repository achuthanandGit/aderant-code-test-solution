import itertools

def overlap(arg_one, arg_two, min_length):
    """ Return length of longest suffix of 'arg-one' matching a prefix of 'arg_two',
        and the prefix is at least "min_length" characters. 
        If there is no such overlap, 0 is returned. 
    """
    start = 0
    while True:
        start = arg_one.find(arg_two[:min_length], start)
        if start == -1:
            return 0
        if arg_two.startswith(arg_one[start:]):
            return len(arg_one)-start
        start += 1

def pick_maximal_overlap(reads):
    """ Finds the first and second read with maximum overlap.
        Returns two reads with mximum overlap along with that overlap
    """
    read_a, read_b = None, None
    best_overlap_len = 0
    for a, b in itertools.permutations(reads, 2):
        # Calculating the overlap length for each pair
        overlap_len = overlap(a, b, min_length=1)
        """ Checks whether the overlap_len is greater than best_overlap_len
            if it is, then best_overlap_len will be updated with new and
            updates read_a and read_b with new pairs.
            In some cases there may be multiple pairs with same longest overlap length.
            But the first one will be the values that will be returned by the function.
        """
        if overlap_len > best_overlap_len:
            read_a, read_b = a, b
            best_overlap_len = overlap_len
    return read_a, read_b, best_overlap_len

def remove_duplicate_substring(reads):
    """ Return the reads after removing unneccessary fragments that will fully overlap with other
    """
    temp = reads
    for data in reads:
        for t in temp:
            if data is not t and t in data:
                temp.remove(t)
    return temp
