import sys
from readable_size import readable_size


class FTPTracker:
    """Tracks ftp upload and download progress. Displays progress bar

    Args:
        file_size (int): size of tracked file
        bar_length (int, optional): length of output bar. Defaults to 50

    Attributes:
        size_written (int): number of bytes that are already written
        file_size (int): size of tracked file
        bar_length (int, optional): length of output bar. Defaults to 50
    """

    def __init__(self, file_size, bar_length=50):
        self.size_written = 0
        self.file_size = file_size
        self.bar_length = bar_length

    def percentage(self):
        """Returns: completeness percentage in string form."""
        return '{0:.1f}'.format(100 *(self.size_written / float(self.file_size)))

    def bar_filled(self):
        """Returns: rounded value of how much bar is filled"""
        return round(self.bar_length * self.size_written / float(self.file_size))

    def bar_string(self):
        """Returns: bar string format"""
        bar_filled = self.bar_filled()
        bar = '#' * bar_filled + '-' * (self.bar_length - bar_filled)
        return '\r |{}| {}% {}/{}'.format(bar, self.percentage(), readable_size(self.size_written),
                                          readable_size(self.file_size))

    def handle(self, block):
        """Handles bar output"""
        self.size_written += len(block)
        sys.stdout.write(self.bar_string())
        if self.size_written == self.file_size:
            sys.stdout.write('\n')
        sys.stdout.flush()
