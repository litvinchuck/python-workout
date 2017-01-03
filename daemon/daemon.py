import os
import sys
import signal


class Daemon:
    """Base for a UNIX daemon. Only function to be run is required. Doesn't meant to be instantiated, use DaemonBuilder
    instead. Mostly created from this guide http://www.netzmafia.de/skripten/unix/linux-daemon-howto.html

    Args:
        main_function(function) - function to be run by the daemon, should accept stdin, stdout, stderr as arguments
        pidfile(str) - file containing the process identification number (pid)
        stdin(str) - standard input stream fil
        stdout(str) - standard output stream file
        stderr(str) - standard error stream file

    Attributes:
        main_function(function) - function to be run by the daemon, should accept stdin, stdout, stderr as arguments
        pidfile(str) - file containing the process identification number (pid)
        stdin(str) - standard input stream file
        stdout(str) - standard output stream file
        stderr(str) - standard error stream file
    """

    def __init__(self, main_function, pidfile, stdin, stdout, stderr):
        self.main_function = main_function
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
        stdin_file = open(self.stdin, 'r')
        stdout_file = open(self.stdout, 'a')
        stderr_file = open(self.stderr, 'a+')
        os.dup2(stdin_file.fileno(), sys.stdin.fileno())
        os.dup2(stdout_file.fileno(), sys.stdout.fileno())
        os.dup2(stderr_file.fileno(), sys.stdout.fileno())

        pidfile = open(self.pidfile, 'w+')
        pidfile.write('{}\n'.format(os.getpid()))
        pidfile.flush()
        return stdin_file, stdout_file, stderr_file

    def getpid(self):
        """Returns pid of the process if it is running. Returns None otherwise"""
        try:
            pidfile = open(self.pidfile)
            pid = int(pidfile.read().strip())
            pidfile.flush()
        except IOError:
            pid = None
        return pid

    def start(self):
        """Starts the daemon process and runs the main function"""
        if self.getpid():
            sys.stderr.write('Daemon is already running')
            sys.exit(1)

        stdin_file, stdout_file, stderr_file = self.fork()
        self.main_function(stdin_file, stdout_file, stderr_file)

    def stop(self):
        """Stops the daemon and performs cleaning up"""
        pid = self.getpid()
        if not pid:
            sys.stderr.write('Daemon is not running')
            sys.exit(1)

        os.kill(pid, signal.SIGTERM)
        os.remove(self.pidfile)
        os.remove(self.stdout)

    def restart(self):
        """Restarts daemon"""
        self.stop()
        self.start()
