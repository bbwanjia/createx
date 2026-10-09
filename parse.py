"""Implement the commands accepted by createx."""

import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

from action import Action
from base import TEX_TYPES

try:
    import settings as config
except ModuleNotFoundError as exc:
    if exc.name != "settings":
        raise
    import settingsexample as config


TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"
PLACEHOLDER = re.compile(r"\*\*([A-Za-z]+)\*\*")
TEX_SPECIAL = re.compile(r"[\\{}$&#%_^~]")
TEX_ESCAPES = {
    "\\": r"\textbackslash{}",
    "{": r"\{",
    "}": r"\}",
    "$": r"\$",
    "&": r"\&",
    "#": r"\#",
    "%": r"\%",
    "_": r"\_",
    "^": r"\textasciicircum{}",
    "~": r"\textasciitilde{}",
}


def extract(commands: list[str]) -> Action:
    return Action(commands)


def Oquit() -> int:
    print("EXIT")
    return 0


def Ocreate(tpe: str, path: str, title: str) -> int:
    destination = Path(path)
    if tpe not in TEX_TYPES:
        print(f"Unknown template: {tpe}")
        return 1
    template = TEMPLATE_DIR / f"{tpe}.tex"
    try:
        source = template.read_text(encoding="utf-8")
        values = {
            "author": str(config.author),
            "date": str(config.date),
            "headerL": str(config.headerL),
            "headerR": str(config.headerR),
            "footer": str(config.footer),
            "title": TEX_SPECIAL.sub(lambda match: TEX_ESCAPES[match.group()], title),
            "beamertheme": str(config.beamertheme),
            "documentclass": "article",
            "Contents": "",
        }
        generated = PLACEHOLDER.sub(lambda match: values.get(match.group(1), match.group()), source)
        with destination.open("x", encoding="utf-8") as output:
            output.write(generated)
    except FileExistsError:
        print(f"{destination} already exists!")
        return 1
    except OSError as exc:
        print(f"Could not create {destination}: {exc}")
        return 1
    print("Created TEX file", destination)
    return 0


def _run(command: list[str]) -> int:
    try:
        return subprocess.run(command, check=False).returncode
    except OSError as exc:
        print(f"Could not run {command[0]}: {exc}")
        return 1


def Oedit(path: str) -> int:
    return _run(["vim", path])


def Omake(path: str) -> int:
    return _run(["pdflatex", path])


def Oopen(path: str) -> int:
    if sys.platform == "darwin":
        return _run(["open", path])
    if os.name == "nt":
        try:
            os.startfile(path)
            return 0
        except OSError as exc:
            print(f"Could not open {path}: {exc}")
            return 1
    opener = shutil.which("xdg-open")
    if opener is None:
        print("Could not find xdg-open.")
        return 1
    return _run([opener, path])


def Odel(path: str) -> int:
    target = Path(path)
    print("To confirm deleting", path, "type its filename below")
    try:
        answer = input("> ")
    except EOFError:
        return 1
    if answer != target.name:
        print("Deletion cancelled.")
        return 1
    try:
        target.unlink()
    except OSError as exc:
        print(f"Could not delete {path}: {exc}")
        return 1
    print("Deleted", path)
    return 0


def Ohelp() -> int:
    print(f"""SIMPLE HELP PANEL

    create [{'|'.join(TEX_TYPES)}] filepath   Create a TeX file from a template.
    edit filepath                            Edit the file with Vim.
    open filepath                            Open the file with the default application.
    del filepath                             Delete after typing its filename.
    make filepath                            Compile with pdflatex.
    show [w|c]                              Show warranty or contribution details.
    help                                    Show this panel.
    quit                                    Exit the interactive prompt.

    See README.md for more details.""")
    return 0


def Oshow(showoption: str) -> int:
    if showoption == "w":
        print("""createx TeX maker
Copyright (C) 2024  bbwanjia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.""")
    elif showoption == "c":
        print("Contribute through GitHub: <https://github.com/bbwanjia/createx>")
    else:
        print("Unknown show option. For warranty type `show w`; for contribution type `show c`.")
        return 1
    return 0
