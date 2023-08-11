def count_letters(a_string: str) -> dict:
    new_dict = {}
    for i in a_string:
        if i.upper() == i.lower() and not new_dict[i.upper()]:
            new_dict[i.upper()] = 1
        elif i.upper() == i.lower():
            new_dict[i.upper()] +=1
    return new_dict

print(count_letters('Oh my goodness!'))