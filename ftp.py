from ftplib import FTP, error_perm, all_errors
from getpass import getpass
import sys

description = '''
    A minimalistic FTP util. A shell for Python ftplib

    getwelcome - Return the welcome message sent by the server in reply to the initial connection. (This message sometimes contains disclaimers or help information that may be relevant to the user.)
    nlst [directory] - Return a list of file names as returned by the NLST command. The optional argument is a directory to list (default is the current server directory). Multiple arguments can be used to pass non-standard options to the NLST command.
    dir [directory] - Produce a directory listing as returned by the LIST command, printing it to standard output. The optional argument is a directory to list (default is the current server directory).
    cwd [pathname] - Set the current directory on the server.
    mkd [pathname] - Create a new directory on the server.
    pwd - Return the pathname of the current directory on the server.
    rmd [dirname] - Remove the directory named dirname on the server.
    size [filename] - Request the size of the file named filename on the server. On success, the size of the file is returned as an integer, otherwise None is returned. Note that the SIZE command is not standardized, but is supported by many common server implementations.
    delete [filename] - Remove the file named filename from the server. If successful, returns the text of the response.
    quit - Send a QUIT command to the server and close the connection.
    exit - Send a QUIT command to the server and close the connection. Same as quit.
    close - Send a QUIT command to the server and close the connection. Same as quit.
    help - display this help

'''

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
    if command[0] in ('exit', 'quit', 'close'):
        print(ftp.quit())
        sys.exit()
    elif command[0] == 'help':
        print(description)
    else:
        try:
            func = getattr(ftp, command[0])
            print(func(command[1])) if len(command) > 1 else print(func())
        except all_errors as error:
            print(error)
        except AttributeError:
            print('Unknown command')
