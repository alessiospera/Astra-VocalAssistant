import time
import datetime
from src.audio import *

def what_time_is_it(command):
    print(command)
    strTime = datetime.datetime.now()
    answer = ""
    minutes = str(strTime.minute) if len(str(strTime.minute)) == 2 else "0" + str(strTime.minute)
    if "era" in command:
        if strTime=="00":
            answer=f"Era mezzanotte e {minutes}."
            print(f"Erano le 00:{minutes}.") 
        elif strTime=="01":
            answer=f"Era l'una e {minutes}."
            print(answer)  
        else:
            answer=f"Erano le {strTime.hour}:{minutes}."
            print(answer)

    else:
        if strTime=="00":
            answer=f"E' mezzanotte e {minutes}."
            print(f"Sono le 00:{minutes}.")

        elif strTime=="01":
            answer=f"E' l'una : {minutes}."
            print(answer) 

        else:
            answer=f"Sono le {strTime.hour} : {minutes}."
            print(answer)

    return answer
        

def timer():
    return 0