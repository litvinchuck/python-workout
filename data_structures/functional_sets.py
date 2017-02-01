"""Set data-structure in functional style and related functions. Requires python 3.6"""
from typing import NewType, Callable, Any

Set = NewType('Set', Callable[[Any], bool])
Property = NewType('Property', Callable[[Any], bool])


def empty_set() -> Set:
    """Generates empty set

    Returns:
        Set: empty set
    """
    return (lambda other_element: False)


def singleton_set(element: Any) -> Set:
    """Returns one element set

    Args:
        element (Any) - element of the set

    Returns:
        Set: function that checks whether other_element is in set
    """
    return (lambda other_element: element == other_element)


def contains(set: Set, element: Any) -> bool:
    """Indicates if set contains element

    Args:
        set (Set) - set that is being checked
        element (Any) - element against which set is checked

    Returns:
        bool: check result
    """
    return set(element)


def union(first_set: Set, second_set: Set) -> Set:
    """Unions two sets

    Args:
        first_set (Set) - first set that should be unioned
        second_set (Set) - second set that should be unioned

    Returns:
        Set: set created from union of two sets
    """
    return (lambda other_element: first_set(other_element) or second_set(other_element))


def intersection(first_set: Set, second_set: Set) -> Set:
    """Intersects two sets

    Args:
        first_set (Set) - first set that should be intersected
        second_set (Set) - second set that should be intersected

    Returns:
        Set: set created from intersection of two sets
    """
    return (lambda other_element: first_set(other_element) and second_set(other_element))


def difference(first_set: Set, second_set: Set) -> Set:
    """Returns difference of two sets

    Args:
        first_set (Set) - origin set
        second_set (Set) - substracted set

    Returns:
        Set: set created from difference of two sets
    """
    return (lambda other_element: first_set(other_element) and not second_set(other_element))


def filter_set(set: Set, property: Property) -> Set:
    """Returns subset of set for which property holds

    Args:
        set (Set) - origin set
        property (Property) - property which subset should hold

    Returns:
        Set: subset of origin set for which property holds
    """
    return (lambda other_element: set(other_element) and property(other_element))


def generate_set(elements_list: list) -> Set:
    """Generates set from a list of elements

    Args:
        elements_list - list of elements

    Returns:
        Set: set generated from a list of elements
    """
    set = empty_set()
    for element in elements_list:
        set = union(set, singleton_set(element))
    return set

if __name__ == '__main__':

    # test empty set
    set = empty_set()

    for i in range(1000):
        assert not contains(set, i)

    # test generate_set
    set = generate_set([1,2,3])

    assert contains(set, 1)
    assert contains(set, 2)
    assert contains(set, 3)
    assert not contains(set, 4)

    # test union
    set1 = generate_set([1, 2])
    set2 = generate_set([2, 3])

    set_union = union(set1, set2)
    assert contains(set_union, 1)
    assert contains(set_union, 2)
    assert contains(set_union, 3)
    assert not contains(set_union, 4)

    # test intersection
    set1 = generate_set([1, 2])
    set2 = generate_set([2, 3])

    set_intersection = intersection(set1, set2)
    assert not contains(set_intersection, 1)
    assert contains(set_intersection, 2)
    assert not contains(set_intersection, 3)

    # test difference
    set1 = generate_set([1, 2])
    set2 = generate_set([2, 3])

    set_difference = difference(set1, set2)
    assert contains(set_difference, 1)
    assert not contains(set_difference, 2)
    assert not contains(set_difference, 3)

    # test filter
    set = generate_set([1, 2, 3])
    set_property = lambda element: element > 1

    set_filter = filter_set(set, set_property)
    assert not contains(set_filter, 1)
    assert contains(set_filter, 2)
    assert contains(set_filter, 3)
