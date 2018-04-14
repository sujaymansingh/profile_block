import cProfile
import pstats
import sys

from contextlib import contextmanager


@contextmanager
def profile_block(out=None, sort_by="tottime", max_lines=30, strip_dirs=True):
    profiler = ResumableProfiler(out=out, sort_by=sort_by, max_lines=max_lines, strip_dirs=strip_dirs)

    profiler.enable()
    try:
        yield
    finally:
        profiler.disable()
        profiler.output_stats()


class ResumableProfiler():
    def __init__(self, out=None, sort_by="tottime", max_lines=30, strip_dirs=True):
        self.out = out if out else sys.stdout
        self.sort_by = sort_by
        self.max_lines = max_lines
        self.strip_dirs = strip_dirs
        self.profiler = cProfile.Profile()

    def enable(self):
        self.profiler.enable()

    def disable(self):
        self.profiler.disable()

    @contextmanager
    def profile_block(self):
        self.profiler.enable()
        try:
            yield
        finally:
            self.profiler.disable()

    def output_stats(self):
        stats = pstats.Stats(self.profiler, stream=self.out)
        if self.strip_dirs:
            stats = stats.strip_dirs()
        stats = stats.sort_stats(self.sort_by)
        if self.max_lines:
            stats.print_stats(self.max_lines)
        else:
            stats.print_stats()
