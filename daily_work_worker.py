#!/usr/bin/env python3

# Usage
# add alias in .xxxxrc
# alias  <name> = "python3 absolute/path/to/daily_work_worker.py
# author Tobias Frahm

import argparse
import configparser
import getpass
import subprocess
from pathlib import Path


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


def exec_custom_command():
    custom_commands = []
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


def create_backup(source, repo):
    # create daily_work_worker before update/upgrade
    interactive_subprocess("Create Backup of {}".format(source),
                           "borg create --stats --progress {}::{}$(date +%d%m%y) {}".format(repo,
                                                                                            source.replace('/', '_'),
                                                                                            source), True)


def main():
    # system update similar to pacman -Syu.
    interactive_subprocess("Update System?", "yay -Syu", True)
    interactive_subprocess("Failed services?", "systemctl --failed", True)
    interactive_subprocess("Showing journalctl output?", "journalctl -p 3 -xb", False)


if __name__ == '__main__':
    # optional args
    parser = argparse.ArgumentParser(description='daily_work_worker, system update, custom commands',
                                     prog='daily work worker',
                                     usage='python3  daily_work_worker.py [options]')
    parser.add_argument('-c', '--custom', help='custom commands', default='disable', choices=['enable', 'disable'])
    parser.add_argument('-s', '--source', help='folder to daily_work_worker', default='/home', type=str)
    # positional args
    parser.add_argument('repo', help='/path/to/borg/repo')
    args = parser.parse_args()
    for src in args.source.split(','):
        if Path(src).exists():
            create_backup(src, args.repo)
        else:
            raise ValueError("{} not found".format(src))
    main()
    if args.custom.lower() == 'enable':
        exec_custom_command()

    print("All jobs done, have a nice day {}".format(getpass.getuser()))
