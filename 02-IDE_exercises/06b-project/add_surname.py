def add_surname(name_list: list[str]) -> list:
    new_list = [x + " Hoffman" for x in name_list if x[0] == "K"]
    return new_list
