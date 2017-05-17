import json
import logging
from os import path

from IPython import get_ipython, paths

log = logging.getLogger("rlipython")

try:
    FileNotFoundError
except NameError: # python 2
    FileNotFoundError = IOError
    json.decoder.JSONDecodeError = ValueError

_default_warning = """
will just configure the default IPython profile to use it, by editing this
file:

    {}

If you want to set up any *other* profile to use rlipython, you will have to
start IPython using the profile, and then run

    import rlipython; rlipython.install()
"""

_rl_config = "rlipython.TerminalInteractiveShell"
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
    cfg, json_path = get_config()

    installed = cfg.get(app_key, {}).get(shell_key) == _rl_config

    if installed:
        print ("Looks like rlipython is already installed.")
        return

    if get_ipython() is None:
        log.warning(_default_warning + json_path)

    with open(json_path, 'w') as f:
        cfg.update({app_key: {shell_key: _rl_config}})
        json.dump(cfg, f)

    print("Installation succeeded: enjoy rlipython the next time you run ipython!")

def uninstall():
    cfg, json_path = get_config()
    with open(json_path, 'w') as f:
        cfg.get(app_key, {}).pop(shell_key, None)
        json.dump(cfg, f)

    print("Uninstalled rlipython.")
