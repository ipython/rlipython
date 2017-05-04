# rlipython

Up until version 4.2, command-line IPython had a readline frontend, which was
replaced by prompt_toolkit in IPython 5. `rlipython` brings that classic
readline functionality to IPython 5.4+ and 6.0+.

See https://github.com/ipython/ipython/issues/10364 for information.

# Usage

You can try out `rlipython` like this:

```
ipython --TerminalIPythonApp.interactive_shell_class=rlipython.TerminalInteractiveShell
```

# Installation

```python
import rlipython; rlipython.install()
```

This will enable rlipython for the active IPython profile, or the default
profile, if you run it from plain Python.


# Removal
```python
import rlipython; rlipython.uninstall()
```

# License

This code has was extracted from IPython 5.x-dev, so it is under [IPython's
LICENSE](LICENSE.rst)

# Maintenance

This is something that we offer in support of historical compatibility and
certain specific use cases where our main interface (prompt-toolkit) isn't
optimal. But we do not envision any significant development beyond fixing
critical bugs. We only have the resources to offer this as a best-effort
solution.
