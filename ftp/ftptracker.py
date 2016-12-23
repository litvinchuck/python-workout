import sys
from datetime import datetime

from utils.readable import readable_size, readable_time


class FTPTracker:
    """Tracks ftp upload and download progress. Displays progress bar

    Args:
        file_size (int): size of tracked file
        bar_length (int, optional): length of output bar. Defaults to 50

    Attributes:
        size_written (int): number of bytes that are already written
        file_size (int): size of tracked file
        bar_length (int): length of output bar. Defaults to 50
        start_time: ftp transfer start time
    """

    def __init__(self, file_size, bar_length=50):
        self.size_written = 0
        self.file_size = file_size
        self.bar_length = bar_length
        self.start_time = datetime.now()

    def percentage(self):
        """Returns completeness percentage in string form."""
        return '{0:.1f}'.format(100 * (self.size_written / float(self.file_size)))

    def bar_filled(self):
        """Returns rounded value of how much bar is filled"""
        return round(self.bar_length * self.size_written / float(self.file_size))

    def rate(self):
        """Returns transfer rate measured in bytes per second"""
        return self.size_written / (datetime.now() - self.start_time).total_seconds()

    def eta(self):
        """Returns approximately how much time is left"""
        return (self.file_size - self.size_written) / self.rate()

    def bar_string(self):
        """Returns bar string format"""
        bar_filled = self.bar_filled()
        bar = '#' * bar_filled + '-' * (self.bar_length - bar_filled)
        return '\r |{bar}| {percentage}% {size_written}/{file_size} {rate}/s {eta}'.format(
            bar = bar,
            percentage = self.percentage(),
            size_written = readable_size(self.size_written),
            file_size = readable_size(self.file_size),
            rate = readable_size(self.rate()),
            eta = readable_time(self.eta())
        )

    def handle(self, block):
        """Handles bar output"""
        self.size_written += len(block)
        sys.stdout.write(self.bar_string())
        if self.size_written == self.file_size:
            sys.stdout.write('\n')
        sys.stdout.flush()
        sys.stdout.write('\033[K')  # Clears the end of the line to prevent output overlapping
