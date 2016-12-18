"""Functions to convert values to a human readable format"""

import math

size_units = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
time_units = ('s', 'm', 'h')


def readable_base(origin_value, units_set, divisor, precise=False):
    if origin_value <= 1:
        return '{}{}'.format(int(origin_value), units_set[0])

    power = math.floor(math.log(origin_value, divisor))
    if power >= len(units_set):
        power = len(units_set) - 1

    multiple_value = math.floor(origin_value / math.pow(divisor, power))

    if precise:
        zero_value = '0{}'.format(units_set[0])
        sub_result = readable_base(origin_value - multiple_value * math.pow(divisor, power), units_set, divisor).replace(zero_value, '')
    else:
        sub_result = ''

    return '{:g}{} {}'.format(multiple_value, units_set[power], sub_result).rstrip()


def readable_size(byte_value):
    return readable_base(byte_value, size_units, 1024)


def readable_time(seconds_value):
    return readable_base(seconds_value, time_units, 60, precise=True)

if __name__ == '__main__':
    assert readable_size(0) == '0B'
    assert readable_size(1024) == '1KB'
    assert readable_size(104857600) == '100MB'
    assert readable_size(209715200) == '200MB'
    assert readable_size(1073741824000) == '1000GB'

    assert readable_time(0) == '0s'
    assert readable_time(60) == '1m'
    assert readable_time(3600) == '1h'
    assert readable_time(3660) == '1h 1m'
    assert readable_time(216000) == '60h'
