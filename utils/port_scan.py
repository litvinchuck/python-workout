"""Port scanning functions"""
from socket import socket, gethostbyname


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

if __name__ == '__main__':
    assert scan_port('google.com', 80)
    assert scan_port('ftp.debian.org', 80)
    assert scan_port('ftp.debian.org', 21)
    assert scan_port('ftp.debian.org', 22)
