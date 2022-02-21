from abc import ABC, abstractmethod
import re
from typing import Union

class Command(ABC):
    """Abstract class representing a generic command for the Assistant

    Attributes:
        pattern (re.Pattern): regular expression to be matched for the action to be executed
    """

    def __init__(self, pattern: str) -> None:
        """Command class constructor (it cannot be called since this is an abstract class)

        Args:
            pattern (str): target regular expression as a string
        """

        super().__init__()
        self.__pattern: re.Pattern = re.compile(pattern)

    @abstractmethod
    def action(self, match: re.Match) -> str:
        """Action to be performed if the pattern is matched

        Args:
            match (re.Match): Match object with all the matched components of the regular expression

        Returns:
            str: Output text to be spoken by the Assistant
        """

        pass

    def verify(self, text: str) -> Union[str, None]:
        """Verifies if the command pattern is matched

        Args:
            text (str): Input text to be checked

        Returns:
            str | None: Output text to be spoken by the Assistant if the pattern is macthed; None otherwise
        """

        result = self.__pattern.match(text)
        return None if result is None else self.action(result)