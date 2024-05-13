from typing import TextIO


def fprint(where: TextIO, what: str) -> None:
    print(what, file=where)


def write_list(where: TextIO, what: list, end="\n") -> None:
    for item in what:
        print(item, file=where, end=end)
