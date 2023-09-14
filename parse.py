import os
from settings import *
from action import Action


def extract(commands: list[str]) -> Action:
    check = Action.check_eligibility(commands)
    if check:
        raise check
    # passes check
    return Action(commands=commands)


def Oquit() -> int:
    print("EXIT\n\n")
    return 0


def Ocreate(tpe: str, path: str) -> int:
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
    print("See README.md")
    # return os.system("vim README.md")


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
