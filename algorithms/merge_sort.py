"""Merge sort algorithm implementation
Basic idea is that input array is split into halves until base case is hit (array length equals 1) for all branches.
Then all branches from bottom to top are merged to form sorted sub-arrays
Expected performance: O(nlog(n)),
~ log(n) levels of recursion and ~ n operations done at each level
"""

import random
from datetime import datetime
from utils.readable import readable_time


def sort(array):
    """Sorts an array object using merge sort algorithm.
    Splits array in two halves until base case is hit then merges them

    Args:
        array - list object that should be sorted

    Returns:
        list: sorted list object
    """
    array_length = len(array)
    if array_length > 1:
        return merge(sort(array[:(array_length // 2)]), sort(array[(array_length // 2):]))
    else:
        return array


def merge(first_array, second_array):
    """Merges two arrays into one, forming sorted array
    Uses results array for return.

    Args:
        first_array - first merged array
        second_array - second merged array

    Returns:
        list: sorted array containing elements from merged arrays
    """
    result_array = []
    i = j = 0
    while i < len(first_array) or j < len(second_array):
        if i == len(first_array):
            result_array += second_array[j:]
            break
        elif j == len(second_array):
            result_array += first_array[i:]
            break
        elif first_array[i] < second_array[j]:
            result_array.append(first_array[i])
            i += 1
        else:
            result_array.append(second_array[j])
            j += 1
    return result_array

if __name__ == '__main__':

    # test sorted 1 000 000 items list
    sorted_list = list(range(0, 1000000))
    start_time = datetime.now()
    sort(sorted_list)
    print('Sorted 1 000 000 items list:', readable_time((datetime.now() - start_time).total_seconds()))

    # test reversed 1 000 000 items list
    reversed_list = list(range(1000000, 0, -1))
    start_time = datetime.now()
    sort(reversed_list)
    print('Reversed 1 000 000 items list:', readable_time((datetime.now() - start_time).total_seconds()))

    # test shuffled 1 000 000 items list
    random.shuffle(sorted_list)
    shuffled_list = sorted_list
    start_time = datetime.now()
    sort(shuffled_list)
    print('Shuffled 1 000 000 items list:', readable_time((datetime.now() - start_time).total_seconds()))

    # test random 1 000 000 items list in range from -500 000 to 499 999
    random_list = random.sample(range(-500000, 500000), 1000000)
    start_time = datetime.now()
    sort(random_list)
    print('Random 1 000 000 items list in range from -500 000 to 499 999:',
          readable_time((datetime.now() - start_time).total_seconds()))

    # test sorted 1 000 000 items list in range from -500 000 to 499 999
    sorted_random_list = sorted(random.sample(range(-500000, 500000), 1000000))
    start_time = datetime.now()
    sort(sorted_random_list)
    print('Sorted random 1 000 000 items list in range from -500 000 to 499 999:',
          readable_time((datetime.now() - start_time).total_seconds()))

    # test reversed 1 000 000 items list in range from -500 000 to 499 999
    reversed_random_list = list(reversed(random.sample(range(-500000, 500000), 1000000)))
    start_time = datetime.now()
    sort(reversed_random_list)
    print('Reversed random 1 000 000 items list in range from -500 000 to 499 999:',
          readable_time((datetime.now() - start_time).total_seconds()))

    # test list containing one item repeated 1 000 000 times
    random_item = random.randint(-500000, 499999)
    repeated_list = [random_item] * 1000000
    start_time = datetime.now()
    sort(repeated_list)
    print('List containing one item repeated 1 000 000 times:',
          readable_time((datetime.now() - start_time).total_seconds()))
