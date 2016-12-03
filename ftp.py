from ftplib import FTP, error_perm
from getpass import getpass
import sys

print("FTP util\n")

host = input("Enter FTP hostname: ").replace('http://', '').replace('ftp://', '')
user = input("Enter username: ")
password = getpass("Enter password: ")

try:
    ftp = FTP(host)
except:
    print("Error, Host not found")
    input()
    sys.exit()
else:
    print(ftp.getwelcome())

try:
    print(ftp.login(user, password))
except error_perm as error:
    print(error)
    input()
    sys.exit()

while True:
    command = input(">> ").split(" ")
    try:
        func = getattr(ftp, command[0])
        print(func(command[1])) if len(command) > 1 else print(func())
    except:
        continue