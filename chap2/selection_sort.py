import random
from utils import record_time

def find_smallest(arr: list) -> int:
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index

@record_time
def selection_sort(arr: list) -> list:
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


if __name__ == "__main__":
    random_list = [random.randrange(100) for _ in range(10000)]
    sorted_list = selection_sort(random_list)
    another = record_time(sorted)(random_list)
