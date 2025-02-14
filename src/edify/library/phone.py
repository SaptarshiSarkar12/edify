import re

pattern = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"


def phone_number(phone: str) -> bool:
    """Checks if a string is a valid phone number.

    Args:
        phone (str): The string to check.
    Returns:
        bool: True if the string is a valid phone number, False otherwise.
    """

    if re.match(pattern, phone):
        return True
    else:
        return False
