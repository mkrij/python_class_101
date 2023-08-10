def reverse_list (a_list: list[int]) -> None:
    a_list = [x[-1] for x in a_list]

vals = [2, -5, 10, 9]
reverse_list(vals)
print(vals)  # This should print [9, 10, -5, 2]