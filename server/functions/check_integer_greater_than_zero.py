def check_integer_greater_than_zero(value):
    if value < 1:
        raise ValueError(f"{value} is not greater than 0")
    return value