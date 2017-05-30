# -*- coding: utf-8 -*-
""" Imports and provides the 'correct' version of readline for the platform.

In addition to normal readline stuff, this module provides have_readline
boolean and _outputfile variable used in IPython.utils.
"""

import sys
import warnings

_rlmod_names = ['readline', 'gnureadline']

# Test to see if libedit is being used instead of GNU readline.
# Thanks to Boyd Waters for the original patch.
uses_libedit = False
have_readline = False
for _rlmod_name in _rlmod_names:
    try:
        _rl = __import__(_rlmod_name)

        # Official Python docs state that 'libedit' is in the docstring for
        # libedit readline:
        uses_libedit = _rl.__doc__ and 'libedit' in _rl.__doc__
        # Note that many non-System Pythons also do not use proper readline,
        # but do not report libedit at all, nor are they linked dynamically
        # against libedit. Known culprits of this include: EPD, Fink
        # There is not much we can do to detect this, until we find a specific failure
        # case, rather than relying on the readline module to self-identify as broken.

        if sys.platform == "darwin" and uses_libedit:
            # System / Python.org pythons should use gnureadline
            print("will try to use gnureadline")
            continue
        globals().update({k:v for k,v in _rl.__dict__.items() if not k.startswith('_')})
    except ImportError:
        pass
    else:
        have_readline = True
        break

if have_readline and (sys.platform == 'win32' or sys.platform == 'cli'):
    try:
        _outputfile=_rl.GetOutputFile()
    except AttributeError:
        warnings.warn("Failed GetOutputFile")
        have_readline = False


# the clear_history() function was only introduced in Python 2.4 and is
# actually optional in the readline API, so we must explicitly check for its
# existence.  Some known platforms actually don't have it.  This thread:
# http://mail.python.org/pipermail/python-dev/2003-August/037845.html
# has the original discussion.

if have_readline:
    try:
        _rl.clear_history
    except AttributeError:
        def clear_history(): pass
        _rl.clear_history = clear_history
