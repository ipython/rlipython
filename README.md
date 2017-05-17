# rlipython

Up until version 4.2, command-line IPython had a readline frontend, which was
replaced by prompt_toolkit in IPython 5. `rlipython` brings that classic
readline functionality to IPython 5.4+ and 6.0+.

See https://github.com/ipython/ipython/issues/10364 for information.



# Try it out

You can try out `rlipython` like this:

```
ipython --TerminalIPythonApp.interactive_shell_class=rlipython.TerminalInteractiveShell
```

# Do I have to do that every time?

No. To have `rlipython` enabled automatically, do this:

```python
import rlipython; rlipython.install()
```

This will enable `rlipython` for the default IPython profile, if you run it
using plain `python`, or the active profile if you run it from `ipython`.

After running `rlipyton.install()`, you can go back to starting IPython just by
using `ipython` without the extra configuration flag.


# Removal
```python
import rlipython; rlipython.uninstall()
```

## Python 2 or Python 3

`rlipython` will work in both Python 2 and Python 3. However, as of May 15th,
2017, IPython 6.0 is the only released version of IPython which supports a
configurable `interactive_shell_class`, but IPython 6.0 only works in Python 3.
So if you want to use `rlipython` in Python 2, you will have to install the
[IPython 5.x branch from git](https://github.com/ipython/ipython/tree/5.x), or
wait for IPython 5.4 release.

# License

This code has was extracted from IPython 5.x-dev, so it is under [IPython's
LICENSE](LICENSE.rst).
