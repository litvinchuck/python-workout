import signal
from daemon import Daemon
from signal_handler import SignalHandler


class DaemonBuilder:
    """Builder class for Daemon"""

    @staticmethod
    def build(main_function, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        """Builds the daemon and returns DaemonHandler instance

            Args:
                main_function(function) - function to be run by the daemon, should accept stdin, stdout and stderr as arguments
                pidfile(str) - file containing the process identification number (pid)
                stdin(str) - standard input stream file. Defaults to /dev/null
                stdout(str) - standard output stream file. Defaults to /dev/null
                stderr(str) - standard error stream file. Defaults to /dev/null

            Returns:
                DaemonHandler instance
            """
        daemon = Daemon(main_function, pidfile, stdin, stdout, stderr)
        handler = SignalHandler(daemon)
        signal.signal(signal.SIGTERM, handler.handle)
        return handler
