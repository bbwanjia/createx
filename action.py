"""Validate and normalize the existing createx command syntax."""

from dataclasses import dataclass
from pathlib import Path

from base import OPCODES, TEX_TYPES


class CommandError(ValueError):
    """A command cannot be executed as written."""


@dataclass
class Action:
    opcode: str = "noentry"
    path: str = ""
    title: str = ""
    choice: str = ""
    showoption: str = ""

    def __init__(self, commands: list[str]) -> None:
        error = self.check_eligibility(commands)
        if error is not None:
            raise error

        self.opcode = commands[0] if commands else "noentry"
        self.path = self.title = self.choice = self.showoption = ""
        if self.opcode == "show":
            self.showoption = commands[1]
        elif self.opcode == "create":
            self.choice = commands[1]
            self._set_path(commands[2])
        elif self.opcode in {"edit", "make", "open", "del"}:
            self._set_path(commands[1])

    def _set_path(self, filename: str) -> None:
        target = Path(filename).expanduser()
        if target.suffix != ".tex":
            target = Path(str(target) + ".tex")
        self.path = str(target.resolve())
        self.title = target.stem

    @staticmethod
    def check_eligibility(commands: list[str]) -> CommandError | None:
        if not commands:
            return None
        opcode = commands[0]
        if opcode not in OPCODES:
            return CommandError(f"Unknown command '{opcode}'. Type `help` for commands.")
        expected = 3 if opcode == "create" else 2 if opcode in {
            "edit", "make", "open", "del", "show"
        } else 1
        if len(commands) != expected:
            return CommandError(f"Wrong number of arguments for `{opcode}`. Type `help` for usage.")
        if opcode == "create" and commands[1] not in TEX_TYPES:
            return CommandError(
                f"Unknown template '{commands[1]}'. Available templates: {', '.join(TEX_TYPES)}."
            )
        if opcode in {"create", "edit", "make", "open", "del"} and not commands[-1].strip():
            return CommandError("A file path is required.")
        return None
