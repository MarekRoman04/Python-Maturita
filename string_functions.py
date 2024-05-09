def is_digit(string: str) -> bool:
    for char in string:
        if char not in "1234567890":
            return False

    return True


def to_upper(string: str) -> str:
    upper_string = str()

    for char in string:
        if ord(char) > 96 and ord(char) < 123:
            upper_string += chr(ord(char) - 32)
        else:
            upper_string += char

    return upper_string


def to_lower(string: str) -> str:
    lower_string = str()

    for char in string:
        if ord(char) > 64 and ord(char) < 91:
            lower_string += chr(ord(char) + 32)
        else:
            lower_string += char

    return lower_string