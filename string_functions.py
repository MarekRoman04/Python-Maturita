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
    lower_string = ""

    for char in string:
        if ord(char) > 64 and ord(char) < 91:
            lower_string += chr(ord(char) + 32)
        else:
            lower_string += char

    return lower_string

def join(string_list : list[str], separator: str) -> str:
    merged_string = ""
    for string in string_list:
        merged_string += string + separator
    
    return merged_string[:-len(separator)]