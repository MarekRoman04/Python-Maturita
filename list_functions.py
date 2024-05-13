def bubble_sort(lst: list) -> list:
    for i in range(len(lst)):
        for j in range(0, len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def selection_sort(lst: list) -> list:
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


def quick_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst

    pivot = len(lst) // 2
    lower = []
    higher = []

    for i, num in enumerate(lst):
        if i == pivot:
            continue

        if num <= lst[pivot]:
            lower += [num]
        else:
            higher += [num]

    return quick_sort(lower) + [lst[pivot]] + quick_sort(higher)


def find(lst: list, what) -> int:
    for i, item in enumerate(lst):
        if item == what:
            return i

    return -1


def find_all(lst: list, what) -> list[int]:
    indexes = []

    for i, item in enumerate(lst):
        if item == what:
            indexes += [i]

    return indexes if len(indexes) else -1


def count(lst: list, what) -> int:
    count: int = 0

    for item in lst:
        count += 1 if item == what else 0

    return count


def min_index(lst: list[int | float]) -> int:
    index = 0

    for i, num in enumerate(lst):
        if num < lst[index]:
            index = i

    return index


def max_index(lst: list[int | float]) -> int:
    index = 0

    for i, num in enumerate(lst):
        if num > lst[index]:
            index = i

    return index


def sum(lst: list[int | float]) -> int | float:
    sum = 0

    for num in lst:
        sum += num

    return sum


def avg(lst: list[int | float]) -> float:
    sum = 0

    for num in lst:
        sum += num

    return sum / len(lst)
