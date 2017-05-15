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

# License

This code has was extracted from IPython 5.x-dev, so it is under [IPython's
LICENSE](LICENSE.rst).
