import time
import datetime
from src.audio import *

#time_sentence = ["ore", "time", "ora"]

def what_time_is_it(command):
    print(command)
    strTime = datetime.datetime.now()
    answer = ""
    if command == "era":
        if strTime==0:
            answer=f"Era mezzanotte e {strTime.minute}."
            print(answer) 
        elif strTime==1:
            answer=f"Era l'una e {strTime.minute}."
            print(answer)  
        else:
            answer=f"Erano le {strTime.hour} e {strTime.minute}."
            print(answer)

    else:
        if strTime==0:
            answer=f"E' mezzanotte e {strTime.minute}."
            print(answer)

        elif strTime==1:
            answer=f"E' l'una e {strTime.minute}."
            print(answer) 
            
        else:
            answer=f"Sono le {strTime.hour} e {strTime.minute}."
            print(answer)

    return answer
        

def timer():
    return 0