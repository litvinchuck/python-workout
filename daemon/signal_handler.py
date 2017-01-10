import signal


class SignalHandler:
    """Basic signal handler for Daemon

    Args:
        daemon (Daemon) - instance of Daemon class

    Attributes:
        daemon (Daemon) - instance of Daemon class
    """

    def __init__(self, daemon):
        self.daemon = daemon

    def handle(self, signum, frame):
        """Handles signals sent by the OS

        Args:
            signum - number of the received signal
            frame - current stack frame
        """
        if signum == signal.SIGTERM:
            self.stop()

    def start(self):
        """Starts the daemon"""
        self.daemon.start()

    def stop(self):
        """Stops the daemon"""
        self.daemon.stop()

    def restart(self):
        """Restarts the daemon"""
        self.daemon.restart()