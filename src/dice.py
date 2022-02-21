from random import randint
from src.time import *
dice_sentence=["lancia un ","tira un ","fai rotolare un ","scaglia un ", "lanciami un ", "tirami un ", "scagliami un "]
dice_types = { 
	"percentuale": 100,
	"d20": 20,
	"d12": 12,
	"d10": 10,
	"d8": 8,
	"d6": 6,
	"d4": 4,
	"bull": 2  
}#d2 non lo capiva ed essendo solo due valori ho scelto bool (valori true:1 e false:2)
#da migliorare dovrebbe essere 0 e 1

#ho usato answer perchè text_out creava problemi
def dice(text_in):
	for t in dice_types.keys():
		for s in dice_sentence:
			if s + t == text_in:
				rand = randint(1,dice_types[t])
				answer="Sto tirando un " + t
				print("Astra: " + answer)
				speak(answer)
				playsound.playsound('audio/dice.mp3')
				answer= "Il risultato del lancio è " + str(rand)
				print("Astra: " + answer)
				speak(answer)
				return 0
	answer="Non conosco il dado che mi hai chiesto di lanciare."
	print("Astra: " + answer)
	speak(answer)
				
			



