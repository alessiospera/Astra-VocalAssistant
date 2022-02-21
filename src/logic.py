import playsound
from AssistenteVocale import get_audio, speak
from src.command import Command
from enum import Enum
from typing import Dict, List, Union
from src.chatting import *

class AssistantState(Enum):
    """Defines constants for handling the Assistant states

    Values:
        INIT (int): The Assistant has just started
        SLEEP (int): The Assistant is waiting for the "wakeup" command
        LISTEN (int): The Assistant is waiting for any command after waking up
    """

    INIT = 0
    SLEEP = 1
    LISTEN = 2

    def __int__(self) -> int:
        """Represents the enumeration as an integer

        Returns:
            int: Integer representation of the constant
        """

        return self.value

class AssistantLogic:
    """Implements the assistant logic and its finite state machine

    Attributes:
        state (AssistantState): State of the Assistant finite state machine
        wakeup_command (str): Vocal command that wakes up the Assistant
        commands_map (dict of (str, Command)): Data structure that maps keywords to commands (for optimization)
    """

    def __init__(self, welcome_msg: str) -> None:
        """Creates an instance of AssistantLogic

        Args:
            welcome_msg (str): message to be spoken on startup
        """

        self.__state: AssistantState = AssistantState.INIT
        self.__wakeup_command: str = None
        self.__commands_map: Dict[str, Command] = {}
        #self.__welcome_msg = welcome_msg

    def set_wakeup_command(self, wakeup_command: str) -> None:
        """Sets the vocal command to wake up the Assistant

        Args:
            wakeup_command (str): Vocal command to be used to wake up the assistant
        """

        self.__wakeup_command = wakeup_command

    def register_command(self, keywords: List[str], command: Command) -> None:
        """Adds a command to be handled by the Assistant

        Args:
            keywords (list of strings): List of keywords associated to a command
            command (Command): Command object, containing the pattern to be macthed and the action to perform
        """

        # Each keyword can have multiple commands associated to it and each command can have multiple keywords associated to it:
        # create a dictionary where each keyword has a list of commands; a command can be in more than one of these lists
        for word in keywords:
            try:
                self.__commands_map[word].append(command)
            except KeyError:
                self.__commands_map[word] = [command]

    def __init_state(self) -> None:
        """Implements the logic of the INIT state
        """

        # Say "Hi"
        playsound.playsound('audio/avvio.mp3') #suono d'avvio provvisorio
        hello() #qua sarà da inserire user_name dell'utilizzatore così potrà salutarlo per nome
        speak(self.__welcome_msg)
        self.__state = AssistantState.SLEEP

    def __sleep_state(self) -> None:
        """Implements the logic of the SLEEP state
        """
        
        # Get the audio
        text_in: str = get_audio()
        if text_in == "":
            return
        # If the input text is the wakeup command, play a sound and go to the LISTEN state
        if text_in == self.__wakeup_command:
            playsound.playsound("audio/bitUP.mp3")
            self.__state = AssistantState.LISTEN

    def __listen_state(self) -> None:
        """Implements the logic of the LISTEN state
        """
        
        # Get the audio
        text_in: str = get_audio()
        if text_in == "":
            return
        # Get the first word of the sentence and use it to find a possible command
        try:
            first = text_in.split(" ")[0]
            # Iterate through the possible commands
            for command in self.__commands_map[first]:
                # Verify the command and get the output text (None if the pattern is not verified)
                output: Union[str, None] = command.verify(text_in)
                if output is None:
                    continue # go to the next possible command
                speak(output)
                break
        except KeyError: # thrown if the keyword has no associated commands
            speak("Ma parla come mangi!")
        self.__state = AssistantState.SLEEP

    def run(self) -> None:
        """Run the logic of the Assistant
        """

        while True:
            # Execute the logic of the state machine
            [self.__init_state, self.__sleep_state, self.__listen_state][int(self.__state)]()