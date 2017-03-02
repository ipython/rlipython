"""
Readline interface for IPython
"""

version_info = (0,0,1)
__version__ = '.'.join([str(x) for x in version_info])

from .completer import RLCompleter
from .interactiveshell import TerminalInteractiveShell
