def add_surname(name_list: list[str]) -> list:
    """
    Adds the last name 'Hoffman' to any member of a list with a first name beggining with 'K'
    """
    new_list = [x + " Hoffman" for x in name_list if x[0] == "K"]
    return new_list
