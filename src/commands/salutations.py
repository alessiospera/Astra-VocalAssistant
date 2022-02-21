from src.command import Command, re
from random import sample
from typing import List

class salutationsCommand(Command):
    def __init__(self, pattern: str, responses: List[str]) -> None:
        super().__init__(pattern)
        self.__responses = responses

    def action(self, match: re.Match) -> str:
        return sample(self.__responses, 1)[0]

class chattingCommand(Command):
    def __init__(self, pattern: List[str], responses: List[str]) -> None:
        super().__init__(pattern)
        self.__responses = responses

    def action(self, match: re.Match) -> str:
        return sample(self.__responses, 1)[0]