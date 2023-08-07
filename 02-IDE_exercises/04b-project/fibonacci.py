def fibonacci(position: int):
    """Returns the value of the nth position of the Fibonacci sequence"""
    value = 1
    prior_value = 0
    for x in range (1, position):
        value = value + prior_value
        prior_value = value - prior_value
    return value