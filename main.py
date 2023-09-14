import sys
import base
from parse import *
commands = sys.argv[1:]


def main() -> int : 
    act = extract(commands)