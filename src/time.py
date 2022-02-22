import time
import datetime
from src.audio import *
time_sentence = ["che ore sono","what time is it", "che ore sono ora", "quale era l'ora di ieri a quest'ora", "a che ora della giornata siamo"]
def what_time_is_it():
    strTime = datetime.datetime.now()
    answer = ""
    if strTime==0:
        answer=f"E' mezzanotte e {strTime.minute}."
        print(answer) 
        #speak(f"E' mezzanotte e {strTime.minute}.")
    elif strTime==1:
        answer=f"E' l'una e {strTime.minute}."
        print(answer) 
        #speak(f"E' l'una e {strTime.minute}.")  
    else:
        answer=f"Sono le {strTime.hour} e {strTime.minute}."
        print(answer)
        #speak(f"Sono le {strTime.hour} e {strTime.minute}.")

    return answer
        

def timer():
    return 0