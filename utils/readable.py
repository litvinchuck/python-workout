"""Functions to convert values to a human readable format"""

import math

size_units = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
time_units = ('s', 'm', 'h')


def readable_base(origin_value, units_set, divisor):
    """Base function for readable functions. Can be used for units with same divisor.
    Args:
        origin_value - input value in minimal units
        units_set - units string values set
        divisor - units divisor
    Returns:
        str: unit in human readable string form
    """
    if origin_value <= 1:
        return '{}{}'.format(int(origin_value), units_set[0])
    elif math.floor(math.log(origin_value, divisor)) >= len(units_set):
        power = len(units_set) - 1  # if power doesn't have a unit use biggest unit available
    else:
        power = math.floor(math.log(origin_value, divisor))
    multiple_value = math.floor(origin_value / math.pow(divisor, power))
    zero_value = ' 0{}'.format(units_set[0])
    return '{}{} {}'.format(
        multiple_value,
        units_set[power],
        readable_base(origin_value - multiple_value * math.pow(divisor, power), units_set, divisor)
    ).replace(zero_value, '')


def readable_size(byte_value):
    """
    Returns:
        str: byte size in human readable form
    """
    return readable_base(byte_value, size_units, 1024)


def readable_time(seconds_value):
    """
    Returns:
        str: time in human readable form
    """
    return readable_base(seconds_value, time_units, 60)

if __name__ == '__main__':
    assert readable_size(0) == '0B'
    assert readable_size(1024) == '1KB'
    assert readable_size(104857600) == '100MB'
    assert readable_size(209715200) == '200MB'
    assert readable_size(222298112) == '212MB'
    assert readable_size(1073741824000) == '1000GB'

    assert readable_time(0) == '0s'
    assert readable_time(60) == '1m'
    assert readable_time(3600) == '1h'
    assert readable_time(3660) == '1h 1m'
    assert readable_time(4210) == '1h 10m 10s'
    assert readable_time(216000) == '60h'
