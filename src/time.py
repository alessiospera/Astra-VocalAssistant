import time
import datetime
from src.audio import *
timeSentence = ["che ore sono","what time is it", "che ore sono ora", "quale era l'ora di ieri a quest'ora", "a che ora della giornata siamo"]
def what_time_is_it():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sono le {strTime}")
    print(f"Sono le {strTime}")

def timer():
    return 0