import playsound  #possibile grazie al fatto che l'ho installato con !pip install playsound
import speech_recognition as sp #installato con !pip install speechrecognition e anche per pyaudio
from gtts import gTTS #installato con !pip install gtts

def speak(text):
	tts = gTTS(text=text,lang='it') #traduce la lingua in italiano
	filename = "voce.mp3"
	if os.path.exists(filename):
		os.remove(filename)
	if filename != None:
		tts.save(filename)
		playsound.playsound(filename)

def get_audio():
	print("LISTENING...")
	r = sp.Recognizer()
	with sp.Microphone() as source:
		r.adjust_for_ambient_noise(source,duration=0.5)
		audio = r.listen(source, phrase_time_limit=5)
		result = ""
		try:
			result = r.recognize_google(audio, language="it")
			print(result)
			print("PROCESSING...")
		except Exception as e:
			print("Errore di riconoscimento vocale")
			get_audio()
	return result