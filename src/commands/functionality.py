from src.command import Command, re
from random import sample
from typing import List
from src.programs import *
from src.dice import *

class programsCommand(Command):
    def __init__(self, pattern: str, responces:str) -> None:
        super().__init__(pattern)

    def action(self, match: re.Match) -> str:
        return check_programs()

class diceCommand(Command):
    def __init__(self, pattern: list[str], responces:str) -> None:
        super().__init__(pattern)

    def action(self, match: re.Match) -> str:
        return dice()

class timeCommand(Command):
    def __init__(self, pattern: list[str]) -> None:
        super().__init__(pattern)

    def action(self, match: re.Match) -> str:
        return what_time_is_it()