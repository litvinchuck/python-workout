"""Functions to convert values to a human readable format"""

import math

size_units = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
time_units = ('s', 'm', 'h')


def readable_base(origin_value, units_set, divisor):
    if origin_value <= 1:
        return '{}{}'.format(int(origin_value), units_set[0])
    power = math.floor(math.log(origin_value, divisor))
    multiple_value = round(origin_value / math.pow(divisor, power), 2)
    return '{:g}{}'.format(multiple_value, units_set[power])


def readable_size(byte_value):
    return readable_base(byte_value, size_units, 1024)


def readable_time(seconds_value):
    return readable_base(seconds_value, time_units, 60)

if __name__ == '__main__':
    assert readable_size(0) == '0B'
    assert readable_size(1024) == '1KB'
    assert readable_size(104857600) == '100MB'
    assert readable_size(209715200) == '200MB'
    assert readable_size(1073741824000) == '1000GB'
    assert readable_size(1315333734400) == '1.2TB'
