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


def join(string_list: list[str], separator: str) -> str:
    merged_string = ""
    for string in string_list:
        merged_string += string + separator

    return merged_string[: -len(separator)]


def split(string: str, separator: str = " ") -> list[str]:
    splited_list = []
    separator_len = len(separator)
    i = 0
    sub_string = ""

    while i < len(string):
        if string[i : i + separator_len] == separator:
            splited_list += [sub_string]
            i += separator_len
            sub_string = ""
        else:
            sub_string += string[i]
            i += 1
    
    if sub_string:
        splited_list += [sub_string]

    return splited_list


def replace(string: str, old: str, new: str) -> str:
    new_string = ""
    old_len = len(old)
    i = 0

    while i < len(string):
        if string[i : i + old_len] == old:
            new_string += new
            i += old_len
        else:
            new_string += string[i]
            i += 1
    
    return new_string