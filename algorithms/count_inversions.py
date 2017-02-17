"""Count inversions algorithm implementation based on merge sort algorithm
Basic idea is that input array is split into halves until base case is hit (array length equals 1) for all branches.
Then all branches from bottom to top are merged to form sorted sub-arrays and inversions are counted
Expected performance: O(nlog(n)),
~ log(n) levels of recursion and ~ n operations done at each level
"""


def sort_and_count(array):
    """Sorts an array object using merge sort algorithm and counts inversions.
    Splits array in two halves until base case is hit then merges them

    Args:
        array: list object that should be sorted

    Returns:
        tuple: first element is sorted list object, second element is number of inversions. E.g. ([1, 2, 3], 2)
    """
    array_length = len(array)
    if (array_length == 1) or (array_length == 0):
        return array, 0
    else:
        first_half, first_half_inversion_count = sort_and_count(array[:(array_length // 2)])
        second_half, second_half_inversion_count = sort_and_count(array[(array_length // 2):])
        sorted_array, split_inversion_count = merge_and_count_inversions(first_half, second_half)
        return sorted_array, (first_half_inversion_count + second_half_inversion_count + split_inversion_count)


def merge_and_count_inversions(first_array, second_array):
    """Merges two arrays into one, forming sorted array. Counts split inversions
    Uses results array for return.

    Args:
        first_array: first merged array
        second_array: second merged array

    Returns:
        tuple: first element is sorted array containing elements from merged arrays, second element is number of split
            inversions. E.g. ([1, 2, 3], 2)
    """
    result_array = []
    inversion_count = 0
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
            inversion_count += len(first_array) - i
    return result_array, inversion_count

if __name__ == "__main__":
    sorted_array, inversion_count = sort_and_count([6, 5, 4, 3, 2, 1])
    assert inversion_count == 15

    sorted_array, inversion_count = sort_and_count([1, 3, 5, 2, 4, 6])
    assert inversion_count == 3
