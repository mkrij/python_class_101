def recursive_multiply(val1: int, val2: int) -> int:
    """Multiplies val1 and val2 using recursive addition"""
    if val2 == 1:
        return val1
    else: 
        return val1 + recursive_multiply(val1,(val2-1))