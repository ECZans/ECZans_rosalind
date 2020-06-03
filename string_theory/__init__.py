"""
Python packages & modules must be 'initialized' for the importer to be aware of them.

Their parent directories must also be on the PYTHONPATH environment variable (which you can
set in .bash_profile/.bashrc like any other) or on the 'sys.path' - an interpreter-specific
set of locations to look for code. The package 'sys' is a builtin of python that can help
with host system management, incl. manipulating & capturing stdout and stderr streams,
determining operating system, finding installed executables, even exiting out of a running
python session. The 'path' attribute of 'sys' is a comma-delimited python object of the 'list'
type containing all paths in PYTHONPATH, plus the current wd.
"""