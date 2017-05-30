import json
import logging
import sys
from os import path

from IPython import get_ipython, paths
from IPython import version_info as ipython_version

log = logging.getLogger("rlipython")

try:
    FileNotFoundError
except NameError: # python 2
    FileNotFoundError = IOError
    json.decoder.JSONDecodeError = ValueError

DEFAULT_WARNING = """
will just configure the default IPython profile to use it, by editing this
file:

    {}

If you want to set up any *other* profile to use rlipython, you will have to
start IPython using the profile, and then run

    import rlipython; rlipython.install()
"""


OSX_PY36_GNUREADLINE_WARNING = """
On OS X, the latest released version of python-gnureadline is currently broken
for Python3.6 and newer. Relevant bug report:
https://github.com/ludwigschwardt/python-gnureadline/issues/50

If you see errors that crash Python with messages like this:

    python3(35119,0x100fa3310) malloc: *** error for object 0x1044849c8: pointer
    being freed was not allocated
    *** set a breakpoint in malloc_error_break to debug
    Abort trap: 6

You will want to:

    pip install https://github.com/ludwigschwardt/python-gnureadline/archive/master.zip
"""
rl_config = "rlipython.TerminalInteractiveShell"
shell_key = "interactive_shell_class"
app_key = "TerminalIPythonApp"

def get_config():
    ip = get_ipython()

    if ip is None:
        profile_dir = paths.locate_profile()
    else:
        profile_dir = ip.profile_dir.location

    json_path = path.join(profile_dir, "ipython_config.json")

    try:
        with open(json_path, 'r') as f:
            config = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        config = {}
    return config, json_path



def install():
    """Register `rlipython` as the default interactive interface for IPython.

    When you run this inside IPython, the preference gets applied to the
    current IPython profile. When run using plain Python, the preference gets
    applied to the default profile.

    Run `uninstall()` if you ever change your mind and want to revert to the
    default IPython behavior.
    """
    if ipython_version < (5,4):
        print("`rliptyhon` will only work with IPython 5.4. or above. Aborting")
        return

    cfg, json_path = get_config()

    installed = cfg.get(app_key, {}).get(shell_key) == rl_config

    if installed:
        print ("Looks like rlipython is already installed.")
        return

    if get_ipython() is None:
        log.warning(DEFAULT_WARNING + json_path)

    with open(json_path, 'w') as f:
        cfg.update({app_key: {shell_key: rl_config}})
        json.dump(cfg, f)

    print("Installation succeeded: enjoy rlipython the next time you run ipython!")

    if sys.platform == "darwin" and sys.version_info[:2] >= (3, 6):
        print(OSX_PY36_GNUREADLINE_WARNING)

def uninstall():
    cfg, json_path = get_config()
    with open(json_path, 'w') as f:
        cfg.get(app_key, {}).pop(shell_key, None)
        json.dump(cfg, f)

    print("Uninstalled rlipython.")
