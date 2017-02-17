""" Closest pair algorithm implementation. Finds closest coordinate pair"""
from math import sqrt


class Point:
    """ Point class representation

    Args:
        x: point x coordinate
        y: point y coordinate

    Attributes:
        x: point x coordinate
        y: point y coordinate
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def distance(first_point, second_point):
    """ Finds the Euclidean distance between points

    Args:
        first_point(Point): first point
        second_point(Point): second point

    Returns:
        distance between points
    """
    return sqrt((first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2)


def find_closest_pair(points):
    """ Finds closest points pair from list of points

    Args:
        points: list of points

    Returns:
        tuple: pair of closest points
    """
    return closest_pair(sorted(points, key=lambda point: point.x), sorted(points, key=lambda point: point.y))


def closest_pair_brute_force(points):
    """ Finds closest pair using brute-force method

    Args:
        points: list of points

    Returns:
        tuple: pair of closest points
    """
    best_distance = distance(points[0], points[1])
    best_points_pair = (points[0], points[1])
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            points_distance = distance(points[i], points[j])
            if points_distance < best_distance:
                best_distance = points_distance
                best_points_pair = (points[i], points[j])
    return best_points_pair


def closest_pair(points_x, points_y):
    """ Finds closest pair using divide and conquer method

    Args:
        points_x: list of points sorted by x coordinate
        points_y: list of points sorted by y coordinate

    Returns:
        tuple: pair of closest points
    """
    if len(points_x) <= 3:
        return closest_pair_brute_force(points_x)
    else:
        points_x_length_half = len(points_x) // 2
        points_x_left = points_x[:points_x_length_half]
        points_x_right = points_x[points_x_length_half:]

        point_y_length_half = len(points_y) // 2
        points_y_left = points_y[:point_y_length_half]
        points_y_right = points_y[point_y_length_half:]

        first_closest_pair = closest_pair(points_x_left, points_y_left)
        second_closest_pair = closest_pair(points_x_right, points_y_right)

        delta = min((distance(*first_closest_pair)), distance(*second_closest_pair))
        third_closest_pair = closest_split_pair(points_x, points_y, delta)

        if third_closest_pair[0] is None:
            return best_pair(first_closest_pair, second_closest_pair, second_closest_pair)
        else:
            return best_pair(first_closest_pair, second_closest_pair, third_closest_pair)


def closest_split_pair(points_x, points_y, delta):
    """ Finds closest pair of points that are split between two halves

    Args:
        points_x: list of points sorted by x
        points_y: list of points sorted by y
        delta: minimal distance between unsplit points

    Returns:
        tuple: pair of closest points
    """
    biggest_left_x = points_x[:len(points_x) // 2][-1]
    in_range_points = []
    for point in points_y:
        if (biggest_left_x.x - delta) <= point.x <= (biggest_left_x.x + delta):
            in_range_points.append(point)

    best_distance = delta
    best_points_pair = (None, None)
    for i in range(len(in_range_points) - 1):
        for j in range(i + 1, min(7, len(in_range_points) - i)):
            first_point, second_point = in_range_points[i], in_range_points[i + j]
            points_distance = distance(first_point, second_point)
            if points_distance < best_distance:
                best_points_pair = (first_point, second_point)
                best_distance = points_distance

    return best_points_pair


def best_pair(first_pair, second_pair, third_pair):
    """ Returns pair of points with lowest distance

    Args:
        first_pair: first pair of points
        second_pair: second pair of points
        third_pair: third pair of points

    Returns:
        pair of points with lowest distance
    """
    return min((first_pair, second_pair, third_pair), key=lambda pair: distance(*pair))

if __name__ == '__main__':
    # test distance function
    assert distance(Point(1, 1), Point(2, 1)) == 1
    assert distance(Point(2, 1), Point(1, 1)) == 1
    assert distance(Point(1, 1), Point(1, 1)) == 0

    # test find closest pair function
    points = [Point(1, 1), Point(2, 2), Point(4, 4), Point(6, 6)]
    assert find_closest_pair(points) == (Point(1, 1), Point(2, 2))

    # test best pair function
    assert best_pair(
        (Point(1, 1), Point(1, 1)),
        (Point(1, 1), Point(2, 2)),
        (Point(1, 1), Point(3, 3))
    ) == (Point(1, 1), Point(1, 1))
