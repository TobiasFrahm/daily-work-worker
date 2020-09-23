#!/bin/python3

# Usage
# add alias in .xxxxrc
# alias  <name> = "python3 absolute/path/to/backup.py
# author Tobias Frahm

import getpass
import subprocess


def interactive_subprocess(question, command, default: bool):
    if default:
        __default = " (Y/n):"
    else:
        __default = " (y/N):"
    res = input(question + __default)
    if "y" in res.lower() or "yes" in res.lower() or default and not res:
        try:
            subprocess.run(command, shell=True)
        except OSError as e:
            print(e)
            exit(-1)


def main():
    # create backup before update/upgrade
    interactive_subprocess("Create Backup",
          "borg create --stats --progress /run/media/frahmt/backup/t495s-frahmt/::home$(date +%d%m%y) /home", True)
    # system update simular to pacman -Syu.
    interactive_subprocess("Update System?", "yay -Syu", True)
    interactive_subprocess("Failed services?", "systemctl --failed", True)
    interactive_subprocess("Showing journalctl output?", "journalctl -p 3 -xb", False)
    print("All jobs done, have a nice day {}".format(getpass.getuser()))


if __name__ == '__main__':
    main()
