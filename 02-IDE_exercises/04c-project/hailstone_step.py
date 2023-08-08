def hailstone_step(num: int) -> int:
    """Returns the number of hailstone steps from a provided number until 1 is reached"""
    counter = 0
    while num:
        if num == 1:
            return counter
        elif num % 2 == 0:
            num /= 2
            counter += 1
        elif num % 2 == 1:
            num = num * 3 + 1
            counter += 1