from base import *
import os


class CommandError(BaseException):
    def __init__(self, *args: object) -> None:
        super()


class Action:
    def __init__(self, commands: list[str]) -> None:
        if commands == []:
            self.opcode = "help"
        else:
            self.opcode = commands[0]
            if commands[-1].endswith(".tex"):
                commands[-1] = ".".join(commands[-1].split(".")[:-1])
            self.title = commands[-1]
            self.path = os.path.abspath(os.path.join(os.getcwd(), commands[-1]))
            if not self.path.endswith(".tex"):
                self.path += ".tex"
            self.choice = None
            if len(commands) == 3:
                self.choice = commands[1]

    @staticmethod
    def check_eligibility(commands: list[str]) -> CommandError:
        tmp = commands.copy()
        l = len(tmp)
        if l == 0:
            return None
        if l > 3:
            return CommandError("Bad command. Use createx help to see help page.")

        if tmp[0] not in OPCODES:
            return CommandError(
                f"Opcode '{tmp[0]}' not understood, opcode must be one of", *OPCODES
            )

        if l == 3 and (tmp[1] not in TEX_TYPES or tmp[0] != "create"):
            return CommandError(f"Cannot give {tmp[1]} to this option. See help page.")

        if l in (1, 2, 3):
            return None
