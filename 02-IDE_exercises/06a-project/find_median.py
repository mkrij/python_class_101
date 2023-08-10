def find_median(num_list:list[int]):
    """
    Returns the median of a list of integers.
    """
    num_list.sort()
    if len(num_list) % 2 == 1:
        return num_list[int((len(num_list)-1)/2)]
    else:
        return (num_list[int(len(num_list)/2)] + num_list[int((len(num_list)-1)/2)])/2
