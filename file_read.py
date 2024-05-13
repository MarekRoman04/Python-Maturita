### STDLIB
from typing import Callable, Any, Generator

### CUSTOM
from string_functions import split as str_split 

def check_extension(file_path: str) -> str:
    if file_path[-4:] != ".txt":
        return file_path + ".txt"
    return file_path

def read_file(file_path: str, encoding="utf-8") -> list:
    data = []

    with open(check_extension(file_path), mode="r", encoding=encoding) as file:
        for line in file:
            data += [line] if line[-1] != "\n" else [line[:-1]]

    return data

# FUNCTION PARAMS:
#   str: file_path (check for extension ".txt")
#   str: encoding (set to "utf-8" by default)
# YIELDS:
#   stripped line
def yield_file_by_line(file_path: str, encoding="utf-8") -> Generator:
    with open(check_extension(file_path), mode="r", encoding=encoding) as file:
        for line in file:
            yield line if line[-1] != "\n" else line[:-1]

# FUNCTION PARAMS:
#   str: file_path (checked for extension ".txt")
#   str: encoding (set to "utf-8" by default)
#   function: line_parser (set to string_functions.split by default)
# RETURNS:
#   list of Any (marked as "Any" since the line_parser does not have to return "str")
def read_file_by_line(file_path: str, encoding="utf-8", line_parser: Callable[[str], Any] = str_split) -> list[Any]:
    data = []

    with open(check_extension(file_path), mode="r", encoding=encoding) as file:
        for line in file:
            data += [line_parser(line)] if line[-1] != "\n" else [line_parser(line[:-1])]

    return data
