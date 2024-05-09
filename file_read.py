def read_file(file_path: str, encoding="utf-8") -> list:
    data = []

    with open(file_path, mode="r", encoding=encoding) as file:
        for line in file:
            data += [line] if line[-1] != "\n" else [line[:-1]]

    return data