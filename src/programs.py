import os
from src.audio import *
#anche questi
open_sentence=["apri","avvia","lancia"] #ho dovuto togliere lancia come comando perché con il nuovo refactoring con il termine lancia, andava ad avviare qualche programma e a lanciare i dadi
close_sentence=["chiudi","termina","killa"]
#questo andrà in un file json	
programs = {
	"twitch": r"D:/Programmi/Twitch/Bin/Twitch.exe",
	"spotify": r"C:/Users/Spera/AppData/Roaming/Spotify/Spotify.exe",
	"steam": r"D:/Programmi/Steam.exe", 
	"new world": r"F:/Giochi/Steam/steamapps/common/New World/NewWorldLauncher.exe",
	"death stranding": r"F:/Giochi/Steam/steamapps/common/Death Stranding/ds.exe",
	"league of legends": r"D:/Giochi/Riot Games/League of Legends/LeagueClient.exe",
	"stadia": r"C:/Program Files (x86)/Google/Chrome/Application",
	"horizon zero dawn": r"F:/Giochi/Steam/steamapps/common/Horizon Zero Dawn",
	"rocket league": r"D:/Programmi/Steam/steamapps/common/rocketleague/Binaries"
} #\\ per windows per evitare che nei path i \n o altro confondano il sistema
  #lo ho cambiato da array di tuple in dizionario per poter selezionare il programma tramite il suo nome come chiave

#ho usato answer perchè text_out creava problemi
def check_programs(command,program):
	answer = " "
	if command in open_sentence: #uniamo la parola di avvio al nome del programma
		answer="Sto aprendo " + program
		print("Astra: " + answer)
		os.startfile(programs[program]) #programs[name]: path programma
		
	elif command in close_sentence:
		answer="Sto chiudendo " + program
		print("Astra: " + answer)
		os.system("TASKKILL /F /IM " + os.path.basename(programs[program]))

	return answer # la funzione deve tornare la stringa da dire, se no può crashere(se nessuna stringa in ritorno)
		
	
