# A context manager for profiling blocks of code

This allows you to use `cProfile` around blocks of code.


## Simple Usage

By default, the output is written to stdout

```
>>> import time
>>> from profile_block import profile_block
>>> with profile_block():
...     time.sleep(2)
... 
         6 function calls in 2.002 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.002    2.002    2.002    2.002 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 contextlib.py:85(__exit__)
        1    0.000    0.000    0.000    0.000 __init__.py:31(disable)
        1    0.000    0.000    0.000    0.000 __init__.py:8(profile_block)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.next}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

You can tell it where to write:

```
>>> output_file = open("blah.log", "w")
>>> with profile_block(out=output_file):
...     # Your code here...
```

Other options:
- `out`: the file-like object to send the profile output to (default: `sys.stdout`)
- `sort_by`: the argument to sort the stats by (default: `tottime`)
- `max_lines`: how many lines to output (default: 30, use `None` for unlimited)
- `strip_dirs`: whether to strip directories from filenames (default: True)


## Turning it on and off again...

```
>>> from profile_block import ResumableProfiler
>>> p = ResumableProfiler()
>>> for i in range(3):
...     time.sleep(5)  # This won't be profiled
...     with p.profile_block():
...         time.sleep(i / 10)  # This will
... 
>>> p.output_stats()
         15 function calls in 0.300 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.300    0.100    0.300    0.100 {built-in method time.sleep}
        3    0.000    0.000    0.000    0.000 __init__.py:34(profile_block)
        3    0.000    0.000    0.000    0.000 contextlib.py:85(__exit__)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.next}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
