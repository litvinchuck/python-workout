"""Converts file size in bytes to a human readable format"""

import math

size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')


def readable_size(byte_value):
    if byte_value == 0:
        return '0B'
    power = math.floor(math.log(byte_value, 1024))
    multiple_value = round(byte_value / math.pow(1024, power), 2)
    return '{:g}{}'.format(multiple_value, size_name[power])

if __name__ == '__main__':
    assert readable_size(0) == '0B'
    assert readable_size(1024) == '1KB'
    assert readable_size(104857600) == '100MB'
    assert readable_size(209715200) == '200MB'
    assert readable_size(1073741824000) == '1000GB'
    assert readable_size(1315333734400) == '1.2TB'
