import wikipedia
from src.audio import *
def search_on_wikipedia(text_in):
    speak("Ricerca su Wikipedia...")
    print("Ricerca su Wikipedia...")
    text_in = text_in.replace("wikipedia", "")
    results = wikipedia.summary(text_in, sentences=3)
    speak("Secondo i dati di Wikipedia ho trovato che: ")
    print("Secondo i dati di Wikipedia ho trovato che: ")
    print(results)
    speak(results)
    return 0
