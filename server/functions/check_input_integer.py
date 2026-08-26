def check_input_integer(value):
    if not isinstance(value, int):
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"{value} is not a number")
    return value