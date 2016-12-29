import os
import sys
import signal

class Daemon:

    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.pidfile = pidfile
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr

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

        # Duplicate daemon file descriptors to standart
        os.dup2(open(self.stdin, 'r').fileno(), sys.stdin.fileno())
        os.dup2(open(self.stdout, 'a').fileno(), sys.stdout.fileno())
        os.dup2(open(self.stderr, 'a+').fileno(), sys.stdout.fileno())

        pidfile = open(self.pidfile)
        pidfile.write('{}\n'.format(os.getpid()))
        pidfile.flush()

    def getpid(self):
        try:
            pidfile = open(self.pidfile)
            pid = int(pidfile.read().strip())
        except IOError:
            pid = None
        finally:
            pidfile.flush()
        return pid

    def start(self, main_function):
        if self.getpid():
            sys.stderr.write('Daemon is already running')
            sys.exit(1)

        self.fork()
        main_function()

    def stop(self):
        pid = self.getpid()
        if not pid:
            sys.stderr.write('Daemon is not running')
            sys.exit(1)

        os.kill(pid, signal.SIGTERM)
        