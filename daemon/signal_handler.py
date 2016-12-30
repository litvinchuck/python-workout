import signal


class SignalHandler:
    """Basic signal handler for Daemon

    Args:
        daemon - instance of Daemon class

    Attributes:
        daemon - instance of Daemon class
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
            self.daemon.stop()
