from src.command import Command, re
from random import sample
from typing import List

class SalutationsCommand(Command):
    def __init__(self, pattern: str, responses: List[str]) -> None:
        super().__init__(pattern)
        self.__responses = responses

    def action(self, match: re.Match) -> str:
        return sample(self.__responses, 1)[0]