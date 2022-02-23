from src.command import Command, re
from random import sample
from typing import List
from src.audio import *

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

class closeCommand(Command):
    def __init__(self, pattern: List[str]) -> None:
        super().__init__(pattern)

    def action(self, match: re.Match) -> str:
        print("Astra: mi sto spegnendo. Ora non potrò più sentirti. A presto caro.")
        speak("Mi sto spegnendo. Ora non potrò più sentirti. A presto caro.")
        playsound.playsound('audio/spegnimento.mp3')
        exit(0)