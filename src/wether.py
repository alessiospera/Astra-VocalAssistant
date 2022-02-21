import json
import webbrowser
import time
import datetime
import requests
from src.audio import *
wether_sentence = ["che tempo fa", "fuori come è il tempo", "come è il meteo", "piove", "c'è il sole"]
def wether():
    api_key="Apply your unique IDS"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("di quale città vuoi sapere il meteo?")
    text_in = get_audio()
    city_name= text_in
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" La temperatura è " +
                str(current_temperature) +
                "\n l'umidità in percentuale " +
                str(current_humidiy) +
                "\n nello specifico  " +
                str(weather_description))
        print(" La temperatura è = " +
                str(current_temperature) +
                "\n umidità (in percentuale) = " +
                str(current_humidiy) +
                "\n nello specifico = " +
                str(weather_description))