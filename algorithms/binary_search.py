"""Binary search implementation. Expected performance O(lg(n))"""


def search(array, element):
    """ Searches array for an element and returns its index

    Args:
        array: searched array
        element: element to search for

    Returns:
        int: element index if element is found, -1 otherwise
    """
    return binary_search(array, element, 0, len(array) - 1)


def binary_search(array, element, min_index, max_index):
    """ Searches array for an element using binary search algorithm and returns its index

    Args:
        array: searched array
        element: element to search for
        min_index: search range minimal index
        max_index: search range maximal index

    Returns:
        int: element index if element is found, -1 otherwise
    """
    if min_index > max_index:
        return -1
    middle_index = (max_index + min_index) // 2
    if array[middle_index] < element:
        return binary_search(array, element, middle_index + 1, max_index)
    elif array[middle_index] > element:
        return binary_search(array, element, min_index, middle_index)
    else:
        return middle_index

if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6]
    for element in array:
        assert search(array, element) == element

    assert search(array, 7) == -1