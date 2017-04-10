# rlipython

This brings the classic readline frontend, which was around in IPython up until
version 4.2 to IPython 5.4+ and 6.0+.

See https://github.com/ipython/ipython/issues/10364 for information. 

# Usage

```
ipython --TerminalIPythonApp.interactive_shell_class=rlipython.TerminalInteractiveShell
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
