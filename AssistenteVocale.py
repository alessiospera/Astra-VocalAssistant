from logging import exception
from src.audio import *
from src.chiacchere import *
from src.programs import *
from src.dice import *
from random import randrange, randint


def check_programs(text_in):
	for p in programs.keys(): #cicla su un array di chiavi(nomi dei programmi)
		for a in avvio:
			if a + p == text_in: #uniamo la parola di avvio al nome del programma
				return 1,p #si possono tornare due variabili
		for c in chiusura:
			if c + p == text_in:
				return 2,p
	return 0,-1

def dice(text_in):
	for d in dice_types.keys():
		for l in lancio:
			if l + d == text_in:
				rand = randint(1,dice_types[d])
				return 1,rand,d
	return 0,0,-1
	

def calcoli(text_in):
	calcolo=["quanto fa ", "che risultato viene se faccio ", "calcolami "]
	playsound.playsound('audio/bitUP.mp3') #ancora da definire la funzione
	return 0

def timer():
	return 0

#Refactoring già pianificato
#main da rifare che è una bruttura, lo so
def main():		#volendo si può evitare ma è norma farlo
	playsound.playsound('audio/avvio.mp3') #suono d'avvio provvisorio
	while True:
		text_in = get_audio()
		text_in = text_in.lower()
		text_out = text_in
		if text_in!=None and text_in != " ":
			if "spegni" == text_in or "arresta" == text_in: #qua c'è una cit
				print("Sperollo: mi sto spegnendo. Ora non potrò più sentirti. A presto caro.")
				speak("Mi sto spegnendo. Ora non potrò più sentirti. A presto caro.")
				playsound.playsound('audio/spegnimento.mp3')
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
			if any([x in text_in for x in avvio]) or any([x in text_in for x in chiusura]):
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
			if any([x in text_in for x in lancio]):
				comand,rand,type = dice(text_in) #comand con una m per differenziare
				if comand == 1:
					text_out="Sto tirando un " + type
					playsound.playsound('audio/dice.mp3')
					print("Sperollo: " + text_out)
					text_out= "Il risultato del lancio è " + str(rand)
					print("Sperollo: " + text_out)

				else:
					text_out="Non conosco il dado che mi hai chiesto di lanciare "
					print("Sperollo: " + text_out)
			
			
			#funzionalità future
				#1 - musica su spotify (avvia spotify, )
				#2 - meteo 
				#3 - ricerche internet

		try:
			#print("*SPEAKING:*")
			speak(text_out)
		except AssertionError:
			speak("Ma parla come mangi!")
			print("Sperollo: Ma parla come mangi!")

if __name__ =='__main__': #questo comando richiama il main solo se il programma viene lanciato tramite cmd con python nomeprogramma.py
	try:
		main()
	except Exception as e:
		print(e)
		#print("Errore generale")
		