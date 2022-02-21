from random import randint
from src.time import *
throw=["lancia un ","tira un ","fai rotolare un ","scaglia un ", "lanciami un ", "tirami un ", "scagliami un "]
comand = 0
def dice(text_in):
	for d in dice_types.keys():
		for l in throw:
			if l + d == text_in:
				rand = randint(1,dice_types[d])
				comand,rand,type = 1,rand,d
	if comand == 1:
		text_out="Sto tirando un " + type
		playsound.playsound('audio/dice.mp3')
		print("Astra: " + text_out)
		text_out= "Il risultato del lancio è " + str(rand)
		print("Astra: " + text_out)

	else:
		text_out="Non conosco il dado che mi hai chiesto di lanciare "
		print("Astra: " + text_out)

dice_types = { 
	"percentuale": 100,
	"d20": 20,
	"d12": 12,
	"d10": 10,
	"d8": 8,
	"d6": 6,
	"d4": 4,
	"bull": 2  
}
#d2 non lo capiva ed essendo solo due valori ho scelto bool (valori true:1 e false:2) 
#da migliorare dovrebbe essere 0 e 1
#randrange esclude l'estremo (potrei utilizzare randint per risolvere il problema) V