"""Command line and interactive entry point."""

import shlex
import sys

from action import CommandError
from parse import Ocreate, Odel, Oedit, Ohelp, Omake, Oopen, Oquit, Oshow, extract


NOTICE = """createx  Copyright (C) 2024  bbwanjia
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
"""


def run(commands: list[str]) -> int:
    try:
        action = extract(commands)
    except CommandError as exc:
        print(exc)
        return 1

    if action.opcode == "quit":
        return Oquit()
    if action.opcode == "create":
        return Ocreate(action.choice, action.path, action.title)
    if action.opcode == "edit":
        return Oedit(action.path)
    if action.opcode == "make":
        return Omake(action.path)
    if action.opcode == "open":
        return Oopen(action.path)
    if action.opcode == "del":
        return Odel(action.path)
    if action.opcode == "help":
        return Ohelp()
    if action.opcode == "show":
        return Oshow(action.showoption)
    return 0


def main(commands: list[str], oneway: bool = False) -> int:
    print(NOTICE)
    if commands:
        result = run(commands)
        if oneway or not sys.stdin.isatty() or commands[0] == "quit":
            return result
    elif oneway:
        print("Type `help` for commands.")
        return 1

    while True:
        try:
            line = input(" > ")
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        try:
            words = shlex.split(line)
        except ValueError as exc:
            print(f"Invalid input: {exc}")
            continue
        if not words:
            continue
        result = run(words)
        if words[0] == "quit":
            return result
