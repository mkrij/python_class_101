def reverse_list (a_list: list[int]) -> None:
    length: int = len(a_list) - 1
    counter = -1
    middle_list = []
    while length > -1:
            middle_list.append(a_list[counter])
            length -= 1
            counter -=1
    counter2 = 0
    while counter2 < len(a_list):
          a_list[counter2] = middle_list [counter2]
          counter2 += 1
vals = [2, -5, 10, 9,7,6,5,4]
reverse_list(vals)
print(vals)