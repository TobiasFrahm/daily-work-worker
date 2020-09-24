#!/usr/bin/env python3

# Usage
# add alias in .xxxxrc
# alias  <name> = "python3 absolute/path/to/dailywork_worker.py
# author Tobias Frahm

import getpass
import subprocess
import configparser


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


def string_to_bool(__string):
    if "true" == __string.lower():
        return True
    elif "false" == __string.lower():
        return False
    else:
        print(__string)
        raise ValueError("Expected True or False in custom_commands.cfg File")


def main():
    # create backup before update/upgrade
    interactive_subprocess("Create Backup",
                           "borg create --stats --progress /run/media/frahmt/backup/t495s-frahmt/::home$(date +%d%m%y) /home",
                           True)
    # system update similar to pacman -Syu.
    interactive_subprocess("Update System?", "yay -Syu", True)
    interactive_subprocess("Failed services?", "systemctl --failed", True)
    interactive_subprocess("Showing journalctl output?", "journalctl -p 3 -xb", False)
    try:
        custom_commands = configparser.ConfigParser()
        custom_commands.read("custom_commands.cfg")
    except configparser.ParsingError as pe:
        print(pe)
        exit(-1)

    # custom commands
    for section in custom_commands.sections():
        print(custom_commands[section])
        interactive_subprocess(custom_commands[section]['question'], custom_commands[section]['command'],
                               string_to_bool(custom_commands[section]['default']))

    print("All jobs done, have a nice day {}".format(getpass.getuser()))


if __name__ == '__main__':
    main()
