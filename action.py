from base import *
import os
class CommandError(BaseException):
    def __init__(self, *args:object) -> None:
        super()

class Action:
    def __init__(self, commands:list[str]) -> None:
        self.opcode = commands[0]
        self.path = commands[-1]
        self.choice = None
        if len(self) == 3:
            self.choice = commands[1]
    
    @staticmethod
    def check_eligibility(commands:list[str]) -> CommandError|None:
        tmp = commands.copy()
        l = len(tmp)
        if l == 0:
            return None
        if l > 3:
            return CommandError("Bad command. Use createx help to see help page.")
        
        if tmp[0] not in OPCODES:
            return CommandError(f"Opcode '{tmp[0]}' not understood, opcode must be one of", *OPCODES)

        if l in (1,2): return None

        if tmp[1] not in TEX_TYPES or tmp[0]!='create':
                return CommandError(f"Cannot give {tmp[1]} to this option. See help page.")
