from logging import exception
import os
import playsound  #possibile grazie al fatto che l'ho installato con !pip install playsound
import speech_recognition as sp #installato con !pip install speechrecognition e anche per pyaudio
from src.chiacchere import *
from src.dice import *
from src.programs import *
from random import randrange 
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

def check_programs(text_in):
	avvio=["apri ","avvia ","lancia "]
	chiusura=["chiudi ","termina ","killa "]
	for p in programs.keys(): #cicla su un array di chiavi(nomi dei programmi)
		for a in avvio:
			if a + p == text_in: #uniamo la parola di avvio al nome dek programma
				return 1,p #si possono tornare due variabili
		for c in chiusura:
			if c + p == text_in:
				return 2,p
	return 0,-1

def dice(text_in):
	lancio=["lancia un ","tira un ","fai rotolare un ","scaglia un "]
	for d in dice_types.keys():
		for l in lancio:
			if l + d == text_in:
				rand = randrange(1,dice_types[d])
				return 1,rand,d
	return 0,-1

def calcoli(text_in):
	calcolo=["quanto fa ", "che risultato viene se faccio ", "calcolami "]
	return 0


def main():		#volendo si può evitare ma è norma farlo
	while True:
		text_in = get_audio()
		text_in = text_in.lower()
		text_out = text_in
		if text_in!=None and text_in != " ":
			if "spegni" == text_in or "arresta" == text_in: #qua c'è una cit
				print("Sperollo: mi sto spegnendo. Ora non potrò più sentirti. A presto caro.")
				speak("Mi sto spegnendo. Ora non potrò più sentirti. A presto caro.")
				break
			if text_in in greetings_in:
				ran = randrange(len(greetings_out))
				text_out = greetings_out[ran]
				print("Sperollo: " + text_out)
			if text_in in convenevoli_in:
				ran = randrange(len(convenevoli_out))
				text_out = convenevoli_out[ran]
				print("Sperollo: " + text_out)
				speak(text_out)
				text_in = get_audio() #ascolta la risposta
				text_in = text_in.lower()
				text_out = text_in
				if text_in in answerPosConve_in:
					ran = randrange(len(answerPosConve_out))
					text_out = answerPosConve_out[ran]
					print("Sperollo: " + text_out)
				elif text_in in answerNegConve_in:
					ran = randrange(len(answerNegConve_out))
					text_out = answerNegConve_out[ran]
					print("Sperollo: " + text_out)
			
			if text_in in casualPosSentence_in:
				ran = randrange(len(casualPosSentence_out))
				text_out = casualPosSentence_out[ran]
				print("Sperollo: " + text_out)
			if text_in in casualNegSentence_in:
				ran = randrange(len(casualNegSentence_out))
				text_out = casualNegSentence_out[ran]
				print("Sperollo: " + text_out)
			if text_in in flaming_in:
				ran = randrange(len(flaming_out))
				text_out = flaming_out[ran]
				print("Sperollo: " + text_out)
			if text_in in motivate_in:
				ran = randrange(len(motivate_out))
				text_out = motivate_out[ran]
				print("Sperollo: " + text_out)
			if text_in in demotivate_in:
				ran = randrange(len(demotivate_out))
				text_out = demotivate_out[ran]
				print("Sperollo: " + text_out)
			
			#FUNZIONALITA'

			#lancio e chiusura programmi
			command,name = check_programs(text_in) #il primo valore di return va in command e il secondo in name
			if  command == 1:
				text_out="Sto aprendo " + name
				print("Sperollo: " + text_out)
				os.startfile(programs[name]) #programs[name]: path programma
			elif command == 2:
				text_out="Sto chiudendo " + name
				print("Sperollo: " + text_out)
				os.system("TASKKILL /F /IM " + os.path.basename(programs[name]))

			#lancio dadi
			comand,rand,type = dice(text_in) #comand con una m per differenziare
			if comand == 1:
				text_out="Sto tirando un " + type
				print("Sperollo: " + text_out)
				text_out= "Il risultato del lancio è " + str(rand)
				print("Sperollo: " + text_out)

			else:
				text_out="Non conosco il dado che mi hai chiesto di lanciare "
				print("Sperollo: " + text_out)



		try:
			#print("*SPEAKING:*")
			speak(text_out)
		except AssertionError:
			speak("Ma parla come mangi!")
			print("Sperollo: Ma parla come mangi!")

if __name__ =='__main__': #questo comando richiama il main solo se il programma viene lanciato tramite cmd con python nomeprogramma.py
	try:
		main()
	except:
		print("Errore generale")