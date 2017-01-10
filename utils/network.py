"""Networking functions"""
from socket import socket, gethostbyname
from http.client import HTTPSConnection, HTTPConnection


def scan_port(host, port):
    """Scans if port is open on specified host.
    Args:
        host(str) - host name or host ip
        port(int) - port number

    Returns:
        True if port is open, False otherwise
    """
    socket_instance = socket()
    host_ip = gethostbyname(host)
    return socket_instance.connect_ex((host_ip, port)) == 0


def network_io():
    """Returns Linux environment network io statistics in dictionary format.
    Where dictionary keys are device names, dictionary values are tuples containing integer values in following order:
        number of bytes sent,
        number of bytes received,
        number of packets sent,
        number of packets received,
        number of errors while receiving,
        number of errors while sending,
        numbers of dropped incoming packets,
        number of dropped outgoing packets
    """
    results_dict = {}
    with open('/proc/net/dev') as file:
        lines = file.readlines()
    for line in lines[2:]:
        colon = line.find(':')
        name = line[:colon].strip()
        stats = line[colon + 1:].split()

        (bytes_recieved, packets_received, err_in, drops_in, fifo_in, frame_in, compressed_in, multicast_in,
            bytes_sent, packets_sent, err_out, drops_out, fifo_out, collisions_out, carrier_out,
            compressed_out) = map(int, stats)

        results_dict[name] = (bytes_sent, bytes_recieved, packets_sent, packets_received, err_in, err_out, drops_in,
                              drops_out)

    return results_dict


def website_status(url):
    """Sends HEAD request to website and returns status
    Args:
        url - website url address with protocol specified

    Returns:
        tuple containing website response code and response status, E.g: (200, 'OK')
    """
    protocol, address = url.split('://')
    if protocol == 'https':
        connection = HTTPSConnection(address)
    else:
        connection = HTTPSConnection(address)
    connection.request('HEAD', '')
    response = connection.getresponse()
    return response.getcode(), response.reason


def website_is_up(url):
    """Checks if website is up
    Args:
        url - website url address with protocol specified

    Returns: True if website is up, False otherwise
    """
    return website_status(url)[0] < 400

if __name__ == '__main__':
    assert scan_port('google.com', 80)
    assert scan_port('ftp.debian.org', 80)
    assert scan_port('ftp.debian.org', 21)
    assert scan_port('ftp.debian.org', 22)

    assert website_is_up('https://www.google.com')
