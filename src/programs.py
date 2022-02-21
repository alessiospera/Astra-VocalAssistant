import os

avvio=["apri ","avvia ","lancia "]
chiusura=["chiudi ","termina ","killa "]

def check_programs(text_in):
	for p in programs.keys(): #cicla su un array di chiavi(nomi dei programmi)
		for a in avvio:
			if a + p == text_in: #uniamo la parola di avvio al nome del programma
				command,name = 1,p #si possono tornare due variabili
		for c in chiusura:
			if c + p == text_in:
				command,name = 2,p
	if  command == 1:
		text_out="Sto aprendo " + name
		print("Astra: " + text_out)
		os.startfile(programs[name]) #programs[name]: path programma
	elif command == 2:
		text_out="Sto chiudendo " + name
		print("Astra: " + text_out)
		os.system("TASKKILL /F /IM " + os.path.basename(programs[name]))
	return 0,-1

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