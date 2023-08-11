def count_letters(a_string: str) -> dict:
    """Takes any string and returns all letters found within the 
    string as well as the number of instances each letter shows up in the string. 
    Not case sensitive
    """
    new_dict = {}
    for i in a_string:
        if 'A' <= i.upper() <= 'Z':
            if i.upper() not in new_dict:
                new_dict[i.upper()] = 1
            elif i.upper() == i.lower().upper():
                new_dict[i.upper()] +=1
    return new_dict
