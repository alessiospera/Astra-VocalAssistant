from random import randint
from src.time import *
dice_sentence=["lancia","tira","rotola","scaglia", "lanciami", "tirami", "scagliami"]
dice_types = { 
	"d100": 100,
	"percentuale":100,
	"d20": 20,
	"d12": 12,
	"d10": 10,
	"d8": 8,
	"d6": 6,
	"d4": 4,
	"d3": 3
}#d2 non lo capiva ed essendo solo due valori ho scelto bool (valori true:1 e false:2)
#da migliorare dovrebbe essere 0 e 1

#ho usato answer perchè text_out creava problemi
def dice(command,num,dice_type):
	answer = ""
	if command in dice_sentence:
		if num == "un":
			num = "1"
		num=int(num)
		dice_type=dice_type.replace("di ","d")
		rolls = [randint(1,dice_types[dice_type]) for _ in range(num)] #_ per evitare l'iterator
		answer="Sto tirando " + str(num) + dice_type
		print("Astra: " + answer)
		speak(answer)
		if(num==1):
			playsound.playsound('audio/dice.mp3')
		else:
			playsound.playsound('audio/moreDice.mp3')
		answer= "Ho tirato "
		for r in rolls:
			answer+= str(r)+", "
		answer+=". Il totale è "+str(sum(rolls))
		print("Astra: " + answer)
	else:
		answer="Non conosco il dado che mi hai chiesto di lanciare."
		print("Astra: " + answer)
	
	return answer
				
			



