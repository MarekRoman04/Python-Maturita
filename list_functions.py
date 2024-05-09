def bubble_sort(list: list) -> list:
    for i in range(len(list)):
        for j in range(0, len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


def selection_sort(list: list) -> list:
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

    return list


def quick_sort(list: list) -> list:
    if len(list) <= 1:
        return list
    
    pivot = len(list) // 2
    lower = []
    higher = []

    for i, num in enumerate(list):
        if i == pivot:
            continue

        if num <= list[pivot]:
            lower += [num]
        else:
            higher += [num]

    return quick_sort(lower) + [list[pivot]] + quick_sort(higher)
