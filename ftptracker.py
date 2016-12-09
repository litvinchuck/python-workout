import sys


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
        """Returns: completeness percentage in float form. Example 0.126"""
        return self.size_written / float(self.file_size)

    def bar_filled(self):
        """Returns: rounded value of how much bar is filled"""
        return round(self.bar_length * self.size_written / float(self.file_size))

    def bar_string(self):
        """Returns: bar string format"""
        bar_filled = self.bar_filled()
        bar = '#' * bar_filled + '-' * (self.bar_length - bar_filled)
        bar_format = '\r |{}| {}%'
        percentage_format = '{0:.1f}'
        return bar_format.format(bar, percentage_format.format(100 * self.percentage()))

    def handle(self, block):
        """Handles bar output"""
        self.size_written += len(block)
        sys.stdout.write(self.bar_string())
        if self.size_written == self.file_size:
            sys.stdout.write('\n')
        sys.stdout.flush()