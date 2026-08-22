import re

def check_data_type_value(allowed_values, value):
    if value not in allowed_values:
        raise ValueError(
            f"{value} is not one of {allowed_values}"
        )
    return value