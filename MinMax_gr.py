import time


def Max_search(arr):
    answer = -1
    for i in range(len(arr)):
        if arr[i] > answer:
            answer = arr[i]
    return answer


def Min_search(arr):
    answer = len(arr)
    for i in range(len(arr)):
        if arr[i] < answer:
            answer = arr[i]
    return answer


array_lengths = list(range(100, 1000, 100))

for length in array_lengths:
    array_to_search = list(range(length))

    # Минимум
    start_time_min = time.time()
    min = Min_search(array_to_search)
    end_time_min = time.time()
    exe_time_min = end_time_min - start_time_min

    # Максимум
    start_time_max = time.time()
    max = Max_search(array_to_search)
    end_time_max = time.time()
    exe_time_max = end_time_max - start_time_max

    print(f"Время выполнения для минимума: {exe_time_min} сек.")
    print(f"Mинимум: {min}.")
    print(f"Время выполнения для максимума: {exe_time_max} сек.")
    print(f"Mаксимум: {max}.\n")
