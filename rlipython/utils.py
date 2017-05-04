import json
import logging
from os import path

from IPython import get_ipython, paths

log = logging.getLogger("rlipython")


_default_warning = """
will just configure the default IPython profile to use it, by editing this
file:

    {}

If you want to set up any *other* profile to use rlipython, you will have to
start IPython using the profile, and then run

    import rlipython; rlipython.install()
"""

_rl_config = "rlipython.TerminalInteractiveShell"

ip = get_ipython()

if ip is None:
    profile_dir = paths.locate_profile()
else:
    profile_dir = ip.profile_dir.location

json_path = path.join(profile_dir, "ipython_config.json")

def get_config():
    try:
        with open(json_path, 'r') as f:
            config = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        config = {}
    return config


def install():
    """Register `rlipython` as the default interactive interface for IPython.

    When you run this inside IPython, the preference gets applied to the
    current IPython profile. When run using plain Python, the preference gets
    applied to the default profile.

    Run `uninstall()` if you ever change your mind and want to revert to the
    default IPython behavior.
    """
    cfg = get_config()

    installed = cfg.get("TerminalIPythonApp",{}).get("interactive_shell_class") == _rl_config

    if installed:
        print ("Looks like rlipython is already installed.")
        return

    if ip is None:
        log.warning(_default_warning + json_path)

    with open(json_path, 'w') as f:
        cfg.update({"TerminalIPythonApp": {"interactive_shell_class":"rlipython.TerminalInteractiveShell"}})
        json.dump(cfg, f)

    print("Installation succeeded: enjoy rlipython the next time you run ipython!")

def uninstall():
    cfg = get_config()
    with open(json_path, 'w') as f:
        cfg.get("TerminalIPythonApp", {}).pop("interactive_shell_class", None)
        json.dump(cfg, f)

    print("Uninstalled rlipython.")
