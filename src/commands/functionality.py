from src.command import Command, re
from random import sample
from typing import List
from src.programs import *
from src.dice import *

class programsCommand(Command):
    def __init__(self, pattern: str) -> None:
        super().__init__(pattern)

    def action(self, match: re.Match) -> str: #match.group(2) nome programma che viene detto (1) sarebbe la prima parola tipo avvia e lo (0) tutto insieme
        return check_programs(match.group(1), match.group(2))

class diceCommand(Command):
    def __init__(self, pattern: str) -> None:
        super().__init__(pattern)

    def action(self, match: re.Match) -> str:
        return dice(match.group(1), match.group(2), match.group(3))

class timeCommand(Command):
    def __init__(self, pattern: str) -> None:
        super().__init__(pattern)

    def action(self, match: re.Match) -> str:
        return what_time_is_it(match.group(2))

# class dayCommand(Command):
#     def __init__(self, pattern: str) -> None:
#         super().__init__(pattern)

#     def action(self, match: re.Match) -> str:
#         return what_time_is_it(match.group(2))