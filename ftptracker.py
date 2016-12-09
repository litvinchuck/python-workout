'''
Tracks ftp upload and download progress. Displays progress bar
'''

import sys


class FTPTracker:

    def __init__(self, file_size, bar_length=50):
        self.size_written = 0
        self.percent_format = '{0:.1f}'
        self.bar_format = '\r |{}| {}%'
        self.file_size = file_size
        self.bar_length = bar_length

    def percentage(self):
        return self.size_written / float(self.file_size)

    def bar_filled(self):
        return round(self.bar_length * self.size_written / float(self.file_size))

    def bar_string(self):
        bar_filled = self.bar_filled()
        bar = '#' * bar_filled + '-' * (self.bar_length - bar_filled)
        return self.bar_format.format(bar, self.percent_format.format(100 * self.percentage()))

    def handle(self, block):
        self.size_written += len(block)
        sys.stdout.write(self.bar_string())
        if self.size_written == self.file_size:
            sys.stdout.write('\n')
        sys.stdout.flush()
