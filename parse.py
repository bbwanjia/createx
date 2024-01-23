import os
from settings import *
from action import Action


def extract(commands: list[str]) -> Action:
    check = Action.check_eligibility(commands)
    if check:
        return Action(commands = [])
    else:
        # passes check
        return Action(commands = commands)


def Oquit() -> int:
    print("EXIT\n\n")
    return 0


def Ocreate(tpe: str, path: str, title: str) -> int:
    if os.path.exists(path):
        print(path + " already exists!")
        return 1

    with open(os.path.join(abspath, "templates", tpe), "r") as raw:
        tex = raw.read()
    tex = tex.replace("**author**", author)
    tex = tex.replace("**date**", date)
    tex = tex.replace("**headerL**", headerL)
    tex = tex.replace("**headerR**", headerR)
    tex = tex.replace("**footer**", footer)
    tex = tex.replace("**title**", title)
    tex = tex.replace("**beamertheme**", beamertheme)

    with open(path, "w") as file:
        file.write(tex)
    print("Created TEX file", path)
    return 0


def Oedit(path: str) -> int:
    return os.system("vim " + path)


def Omake(path: str) -> int:
    return os.system("pdflatex " + path)


def Ohelp() -> int:
    print("""
    SIMPLE HELP PANEL

    - `create [blank|note|article|beamer] filepath` creates a file using templates. Currently there are  four templates: `blank|note|article|beamer`.
    - `edit filepath` opens Vim for editing the file quickly from command prompt.
    - `open filepath` opens the file using default application.
    - `del filepath` deletes the file under second confirmation.
    - `make filepath` complies the file using default $\LaTeX$ complier. Notice that a $\LaTeX$ distribution must be installed on the client and it is not included in this program. TeX Live is recommended.
    - `show [option]` shows details about warranty and contribution, according to the GNU General Public License version 3.0.

    FOR MORE DETAILS PLEASE REFER TO README.md.
""")
    

def Oopen(path: str) -> int:
    return os.system("open " + path)


def Oquit() -> int:
    print("EXIT")
    return 0


def Odel(path: str) -> int:
    print("To confirm deleting", path, "type its filename below")
    res = input("> ")
    if path.endswith(res):
        os.remove(path=path)
    print("Deleted", path)
    return 0

def Oshow(showoption: str) -> int:
    if showoption == "w":
        print("""
createx TeX maker
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
along with this program.  If not, see <https://www.gnu.org/licenses/>.
""")
    elif showoption == "c":
        print("""
Contribute through GitHub: <https://github.com/bbwanjia/createx>
Contact the author by email: <tommy.liu.jingyu@proton.me>
""")
    else:
        print("Unknown show option. For details of warranty type `show w`, for contribution type `show c`.")
