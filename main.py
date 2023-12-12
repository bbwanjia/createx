import base
from parse import *


def main(commands) -> int:
    print("CREATEX tex maker, by bbwanjia.")
    act = extract(commands)
    if act.opcode == "quit":
        return Oquit()
    elif act.opcode == "create":
        return Ocreate(act.choice, act.path, act.title)
    elif act.opcode == "edit":
        return Oedit(act.path)
    elif act.opcode == "make":
        return Omake(act.path)
    elif act.opcode == "open":
        return Oopen(act.path)
    elif act.opcode == "del":
        return Odel(act.path)
    elif act.opcode == "help":
        return Ohelp()
    return 2
