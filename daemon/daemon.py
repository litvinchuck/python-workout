import os
import sys
import signal


class Daemon:
    """Base for a UNIX daemon. Only function to be run is required. Mostly created from this guide http://www.netzmafia.de/skripten/unix/linux-daemon-howto.html

    Args:
        pidfile(str) - file containing the process identification number (pid)
        stdin(str) - standard input stream file. Defaults to /dev/null
        stdout(str) - standard output stream file. Defaults to /dev/null
        stderr(str) - standard error stream file. Defaults to /dev/null

    Attributes:
        pidfile(str) - file containing the process identification number (pid)
        stdin(str) - standard input stream file. Defaults to /dev/null
        stdout(str) - standard output stream file. Defaults to /dev/null
        stderr(str) - standard error stream file. Defaults to /dev/null
    """

    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.pidfile = pidfile
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr

    def fork(self):
        """Forks the daemon process
        Fork a second child and exit immediately to prevent zombies.  This causes the second child process
        to be orphaned, making the init process responsible for its cleanup.
        """
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
        """Returns pid of the process if it is running. Returns None otherwise"""
        try:
            pidfile = open(self.pidfile)
            pid = int(pidfile.read().strip())
        except IOError:
            pid = None
        finally:
            pidfile.flush()
        return pid

    def start(self, main_function):
        """Starts the daemon process and runs the main function

        Args:
            main_function(finction) - function to be run by the daemon
        """
        if self.getpid():
            sys.stderr.write('Daemon is already running')
            sys.exit(1)

        self.fork()

        while True:
            main_function()

    def stop(self):
        """Stops the daemon"""
        pid = self.getpid()
        if not pid:
            sys.stderr.write('Daemon is not running')
            sys.exit(1)

        os.kill(pid, signal.SIGTERM)

    def restart(self):
        """Restarts daemon"""
        self.stop()
        self.start()
