import wikipedia
from src.audio import *
def search_on_wikipedia(text_in):
    speak('Ricerca su Wikipedia...')
    text_in = text_in.replace("wikipedia", "")
    results = wikipedia.summary(text_in, sentences=3)
    speak("In accordo con Wikipedia:")
    print(results)
    speak(results)
