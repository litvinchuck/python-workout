import os
import sys

class Daemon:

    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null', pidfile):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def fork(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as error:
            print('Fork failed:', error)
            sys.exit(1)

        os.umask(0)
        os.chdir('/')
        os.setsid()

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as error:
            print('Fork failed:', error)
            sys.exit(1)

        # Close the standard file descriptors
        sys.stdin.flush()
        sys.stdout.flush()
        sys.stderr.flush()
