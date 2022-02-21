import time
import datetime
from src.audio import *
time_sentence = ["che ore sono","what time is it", "che ore sono ora", "quale era l'ora di ieri a quest'ora", "a che ora della giornata siamo"]
def what_time_is_it():
    strTime = datetime.datetime.now()
    if strTime==0:
        print(f"E' mezzanotte e {strTime.minute}.") 
        speak(f"E' mezzanotte e {strTime.minute}.")
    elif strTime==1:
        print(f"E' l'una e {strTime.minute}.") 
        speak(f"E' l'una e {strTime.minute}.")  
    else:
        print(f"Sono le {strTime.hour} e {strTime.minute}.")
        speak(f"Sono le {strTime.hour} e {strTime.minute}.")
        

def timer():
    return 0