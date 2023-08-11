def reverse_list (a_list: list[int]) -> None:
    length: int = len(a_list) - 1
    counter = -1
    middle_list = []
    while length > -1:
            middle_list.append(a_list[counter])
            length -= 1
            counter -=1
    a_list[:] = middle_list