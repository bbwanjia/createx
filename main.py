from parse import *


def main(commands, oneway = False) -> int:
    print("""
createx  Copyright (C) 2024  bbwanjia
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
""")
    act = extract(commands)
    enter = True
    while enter:
        if act.opcode == "quit":
            enter = False
            Oquit()
            act.opcode = "noentry"
        elif act.opcode == "noentry":
            print("To see help type `help` or see README.md.")
            newline = input(" > ").strip()
            act = extract(newline.split(" "))
        elif act.opcode == "create":
            Ocreate(act.choice, act.path, act.title)
            act.opcode = "noentry"
        elif act.opcode == "edit":
            Oedit(act.path)
            act.opcode = "noentry"
        elif act.opcode == "make":
            Omake(act.path)
            act.opcode = "noentry"
        elif act.opcode == "open":
            Oopen(act.path)
            act.opcode = "noentry"
        elif act.opcode == "del":
            Odel(act.path)
            act.opcode = "noentry"
        elif act.opcode == "help":
            Ohelp()
            act.opcode = "noentry"
        elif act.opcode == "show":
            Oshow(act.showoption)
            act.opcode = "noentry"
        if oneway:
            enter = False
    return 0