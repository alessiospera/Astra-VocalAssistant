from logging import exception
from src.audio import *
from src.chatting import *
from src.programs import *
from src.dice import *
from src.weather import *
from src.search_on_wikipedia import *
from src.time import *
from src.calculator import *
from random import randrange
	

#Refactoring già pianificato
#main da rifare che è una bruttura, lo so
# def main():		#volendo si può evitare ma è norma farlo
# 	#user_name = ""
# 	playsound.playsound('audio/avvio.mp3') #suono d'avvio provvisorio
# 	hello() #qua sarà da inserire user_name dell'utilizzatore così potrà salutarlo per nome
# 	while True:
# 		try:
# 			text_in = get_audio()
# 			text_in = text_in.lower()
# 			text_out = text_in
# 			if text_in!=None and text_in != " ":
# 				if "spegni" == text_in or "arresta" == text_in: #qua c'è una cit
# 					print("Astra: mi sto spegnendo. Ora non potrò più sentirti. A presto caro.")
# 					speak("Mi sto spegnendo. Ora non potrò più sentirti. A presto caro.")
# 					playsound.playsound('audio/spegnimento.mp3')
# 					break
# 				if text_in in greetings_in:
# 					ran = randrange(len(greetings_out))
# 					text_out = greetings_out[ran]
# 					print("Astra: " + text_out)
# 					speak(text_out)
# 				if text_in in convenevoli_in:
# 					ran = randrange(len(convenevoli_out))
# 					text_out = convenevoli_out[ran]
# 					print("Astra: " + text_out)
# 					speak(text_out)
# 					text_in = get_audio() #ascolta la risposta
# 					text_in = text_in.lower()
# 					text_out = text_in
# 					if text_in in answerPosConve_in:
# 						ran = randrange(len(answerPosConve_out))
# 						text_out = answerPosConve_out[ran]
# 						print("Astra: " + text_out)
# 						speak(text_out)
# 					elif text_in in answerNegConve_in:
# 						ran = randrange(len(answerNegConve_out))
# 						text_out = answerNegConve_out[ran]
# 						print("Astra: " + text_out)
# 						speak(text_out)
				
# 				if text_in in casualPosSentence_in:
# 					ran = randrange(len(casualPosSentence_out))
# 					text_out = casualPosSentence_out[ran]
# 					print("Astra: " + text_out)
# 					speak(text_out)
# 				if text_in in casualNegSentence_in:
# 					ran = randrange(len(casualNegSentence_out))
# 					text_out = casualNegSentence_out[ran]
# 					print("Astra: " + text_out)
# 					speak(text_out)
# 				if text_in in flaming_in:
# 					ran = randrange(len(flaming_out))
# 					text_out = flaming_out[ran]
# 					print("Astra: " + text_out)
# 					speak(text_out)
# 				if text_in in motivate_in:
# 					ran = randrange(len(motivate_out))
# 					text_out = motivate_out[ran]
# 					print("Astra: " + text_out)
# 					speak(text_out)
# 				if text_in in demotivate_in:
# 					ran = randrange(len(demotivate_out))
# 					text_out = demotivate_out[ran]
# 					print("Astra: " + text_out)
# 					speak(text_out)
# 				if text_in in who_what_iam:
# 					print("Astra: " + who_what_iam_answer)
# 					speak(who_what_iam_answer)
					
# 				if text_in in who_your_creator:
# 					print("Astra: " + who_your_creator_answer)
# 					speak(who_your_creator_answer)
					
# 				if text_in in new_features:
# 					print("Astra: " + new_features_answer)
# 					speak(new_features_answer)
					
# 				if text_in in future_features:
# 					print("Astra: " + future_features_answer)
# 					speak(future_features_answer)
					

# 				#RICERCHE

# 				#wikipedia
# 				#internet

# 				#FUNZIONALITA'

# 				#che ore sono
# 				if text_in in timeSentence:
# 					what_time_is_it()

# 				#lancio e chiusura programmi
# 				if any([x in text_in for x in open_sentence]) or any([x in text_in for x in close_sentence]):
# 					check_programs(text_in) #il primo valore di return va in command e il secondo in name
					
# 				#lancio dadi
# 				if any([x in text_in for x in dice_sentence]):
# 					dice(text_in)

# 				#calcolatrice
# 				if any([x in text_in for x in calculation_sentence]):
# 					calcoli(text_in)

# 				#meteo
# 				if any([x in text_in for x in wether_sentence]):
# 					wether(text_in) #passo text_in perché vorrei che non richiedesse di quale città si vuole sapere il meteo
			
		
# 			#speak(text_out)
# 		except AssertionError:
# 			print("Astra: Ma parla come mangi!")
# 			speak("Ma parla come mangi!")

from src.commands.salutations import *
from src.commands.functionality import *
from src.logic import *
def main():
	#settaggio assistente
	assistant = AssistantLogic()
	assistant.set_wakeup_command("astra")

	#settaggio chatting
	greetings = salutationsCommand("^(ciao|buongiorno)( astra)?",greetings_out)
	assistant.register_command(["ciao","buongiorno"],greetings)
	# convenevoli = chattingCommand(convenevoli_in,convenevoli_out)
	# assistant.register_command(convenevoli_in,convenevoli)
	# answerPosConve = chattingCommand(answerPosConve_in,answerPosConve_out)
	# assistant.register_command(answerPosConve_in,answerPosConve)
	# answerNegConve = chattingCommand(answerNegConve_in,answerNegConve_out)
	# assistant.register_command(answerNegConve_in,answerNegConve)
	# casualPosSentence = chattingCommand(casualPosSentence_in,casualPosSentence_out)
	# assistant.register_command(casualPosSentence_in,casualPosSentence)
	# casualNegSentence = chattingCommand(casualNegSentence_in,casualNegSentence_out)
	# assistant.register_command(casualNegSentence_in,casualNegSentence)
	# flaming = chattingCommand(flaming_in,flaming_out)
	# assistant.register_command(flaming_in,flaming)
	# motivate = chattingCommand(motivate_in,motivate_out)
	# assistant.register_command(motivate_in,motivate)
	# demotivate = chattingCommand(demotivate_in,demotivate_out)
	# assistant.register_command(demotivate_in,demotivate)
	# who_what_iam = chattingCommand(who_what_iam_in,who_what_iam_out)
	# assistant.register_command(who_what_iam_in,who_what_iam)
	# who_your_creator = chattingCommand(who_your_creator_in,who_your_creator_out)
	# assistant.register_command(who_your_creator_in,who_your_creator)
	# new_features = chattingCommand(new_features_in,new_features_out)
	# assistant.register_command(new_features_in,new_features)
	# future_features = chattingCommand(future_features_in,future_features_out)
	# assistant.register_command(future_features_in,future_features)

	#settaggio funzionalità
	dice_command = diceCommand("^(lancia|tira|fai rotolare|scaglia|lanciami|tirami|scagliami) (un|\d+) (di \d{1,3}|d\d{1,3}|percentuale)") #per programs e dice servirà text_in trovare il modo
	assistant.register_command(["lancia","tira","rotola","scaglia","lanciami","tirami","scagliami"],dice_command)
	programs_command = programsCommand("^(avvia|apri|lancia|chiudi|termina|chilla) (.*)") #per programs e dice servirà text_in trovare il modo
	assistant.register_command(["avvia","apri","lancia","chiudi","termina","chilla"],programs_command)
	
	#time_command = timeCommand(time_sentence)
	#assistant.register_command(time_sentence,time_command)
	
	#avvio ASTRA
	assistant.run()

			

if __name__ =='__main__': #questo comando richiama il main solo se il programma viene lanciato tramite cmd con python nomeprogramma.py
	try:
		main()
	except Exception as e:
		print(e)
		#print("Errore generale") da riattivare solo quando verrà rilasciato agli utenti
		