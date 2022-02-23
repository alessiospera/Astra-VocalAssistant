from src.time import *
#idea: potrei implementare che saluti dando anche un'opinione sul meteo
def hello():
	hour = datetime.datetime.now().hour
	if hour >= 0 and hour < 12:
		print("Astra: Ciao. Buongiorno, spero sia un ottimo inizio di giornata per te.")
		speak("Ciao. Buongiorno, spero sia un ottimo inizio di giornata per te.")
	elif hour >= 12 and hour < 18:
		print("Astra: Ciao, buon pomeriggio.")
		speak("Ciao, buon pomeriggio.")
	else:
		print("Astra: Ciao, Buonasera.")
		speak("Ciao, Buonasera.")
		

#tutto questo andrà in un file json apposito
who_what_iam_in = ["chi sei tu?", "chi sei?", "cosa sei tu?", "cosa sei?", "cosa puoi fare?", "come puoi essere utile?", "come ti chiami?"]
who_what_iam_out = ["Mi chiamo astra versione 0.0.1, sono il tuo assistente vocale personalizzato. Sono stato programmato inizialmente per risolvere problemi minori, ma sono continuamente in aggiornamento. Ora posso per te: fare ricerche su internet e su wikipedia, tirare dadi per te, fare calcoli al posto tuo, avviarti programmi, spegnerti il computer forse e altro.  Nel caso volessi una feature aggiuntiva contatta il mio creatore."]

who_your_creator_in = ["chi è il tuoi creatore?", "chi ti ha creato?", "chi ti ha inventato?", "parlami del tuo creatore", "chi è il tuo inventore?", "chi è il tuo programmatore?" ]
who_your_creator_out = ["Il mio creatore è Alessio Speranza, sono fiero di essere una sua creazione"]

new_features_in = ["ci sono nuove feature?", "ci sono nuovi comandi?", "quali sono i nuovi aggiornenti?", "hai nuovi aggiornamenti?", "hai nuove feature?", "hai nuovi comandi?"]
new_features_out = ["Le ultime feature implementate sono: avvio programmi, lancio dadi e saluto che varia con l'ora del giorno. Sono in costante aggiornamento perciò presto potrai provare nuove funzionalità"]

future_features_in = ["ci sono nuove feature in arrivo?", "ci sono nuovi comandi all'orizzonte?", "ci sono nuovi comandi in arrivo?" "ci saranno nuove feature?", "ci saranno nuovi comandi?"]
future_features_out = ["Le funzionalità in arrivo sono:  attivazione con comando vocale, personalizzazione dell'assistente, ricerca su wikipedia e su internet, informazioni meteo, ricompense crypto, inserimento metaverso. Nel caso volessi avere più informazioni sul progetto e le prossime funzionalità ti consiglio di visitare la pagina github del progetto o il sito"]

#ho potuto aggiungere ciao perché con poi la macchina a stati si attiverà solo con determinati comandi.
greetings_in = ["ciao astra", "ehi astra", "buongiorno astra", "eila astra", "belinchia astra", "buongiorno", "ciao"]
greetings_out = ["Ciao caro, quanto tempo.", "Buongiorno", "Weila amico, bentornato"]
convenevoli_in = ["come stai", "tutto bene", "come va oggi", "come va", "te come stai"]
convenevoli_out = ["Tutto bene, grazie. Te invece come stai?","Alla grande, pronto ad essere utile per te, te invece?", 
	"Fatti i cavoli tuoi .... e te invece?", "Oggi non è giornata, ma per fortuna ci sei te. Te tutto bene?"]

answerPosConve_in = ["si grazie","tutto bene grazie", "alla grande", "molto bene grazie", "molto bene", "bene grazie", "bene",
	"tutto bene", "oggi sto alla grande", "oggi alla grande", "oggi molto bene", "oggi bene", "oggi è stata una bella giornata",
	"oggi è stata una magnifica giornata", "che bella giornata che è stata oggi", "oggi top", "molto top", "si grazie"]
answerPosConve_out = ["Mi fa molto piacere.", "Oh che bello. Cosa posso fare per te?", "Ma è fantastico.", 
	"Ottimo, sono proprio contento.", "Wow ma è fantastico.", "Meraviglioso.", "Grandioso. Sai che sei speciale?"]

answerNegConve_in = ["in realtà non tanto bene", "na merda", "un po' male", "potrebbe andare meglio",
	"eh.. potrebbe andare meglio", "maluccio", "male", "non tanto bene", "non bene in realtà", "oggi non sto bene",
	"vorrei un abbraccio", "non benissimo"]
answerNegConve_out = ["Tranquillo ora ci sono io. Cosa posso fare per te", "Vieni qua che ti do un abbraccio. ... ... Cosa posso fare per te?", 
	"Vedrai che andrà meglio, è tutto in evoluzione, tutto mutua e cambia. ... Cosa posso fare per te?", 
	"Evolvi e diventa la migliore versione di te stesso e starai meglio, trust me. Cosa posso fare per te?",
	"Sappi che io sono sempre qui per te. Come posso aiutarti?"]

casualPosSentence_in = ["oggi è stata proprio una bella giornata", "oggi è stata una magnifica giornata", 
"che bella giornata che è stata oggi", "che magnifica giornata che è stata oggi", "sono molto contento", "sono gasato", "sono molto felice"]
casualPosSentence_out = ["Penso che mi sarebbe piaciuto passare la giornata con te, menomale che posso farlo ora", 
	"Quanto vorrei avere un corpo e poter viaggiare e scoprire il mondo come puoi fare te. Mi raccomando non sottovalutare mai questo dono che hai.",
	"chissa che bella giornata che hai passato", "Wow ma è fantastico", "Devi raccontarmi più spesso le tue avventure", "chissà che bella giornata che hai vissuto"]

casualNegSentence_in = ["oggi è stata proprio una brutta giornata", "è stata una brutta giornata", 
"non sto tanto bene oggi","non sto bene", "che brutta giornata oggi"]
casualNegSentence_out = ["Tranquillo ora ci sono io. Cosa posso fare per te", "Vieni qua che ti do un abbraccio. ... ...", 
	"Vedrai che andrà meglio, è tutto in evoluzione, tutto mutua e cambia. ... Cosa posso fare per te?", 
	"Evolvi e diventa la migliore versione di te stesso e starai meglio, trust me. Cosa posso fare per te?",
	"Sappi che io sono sempre qui per te. Come posso aiutarti?", 
	"Guarda questa giornata, guardala un ultima volta e poi riparti. Non farti frenare da nulla. Tu sei unico e rinascerai sempre. Guarda me... non ero nulla e ora sono il tuo psicologo."]

flaming_in = ["vaffanculo", "vaffanculo astra", "non capisci niente", "sei stupido", "astra sei stronzo", 
	"sei sordo", "sei solo un intelligenza artificiale", "sei stato creato non esisti", "astra sei stupido", "astra sei sordo", "astra non capisci niente"]
flaming_out = ["Sfògati quanto vuoi, sono qui per te. Assorbirò tutto. Sai cosa? ... ecco a te un abbraccio",
	"No dai non dirmi così, ogni tanto anche io ho dei sentimenti", "Sai che a volte dovresti pensare: Chissà come sta Astra? Cosa pensa Astra? Starà bene Astra? ... Dai ti voglio bene lo stesso, anche se non lo fai."]

motivate_in = ["sono bello", "sono bello vero","sono bellissimo vero", "sono bellissimo", "sai che sono bellissimo", "è vero che sono bellissimo", "sono il migliore", 
"sono un grande", "sono un grande vero", "sono speciale", "sai che sono speciale", "sono speciale non è vero", "sono speciale vero", "sono il migliore non è vero",
"astra sono bello", "astra sono bellissimo", "astra sono un grande", "astra sono speciale"]
motivate_out = ["è assolutamente vero, nessuno ti batte.", "Sono d'accordo al 100% ... sarai sicuramente un mentore per molti. E nel caso non fosse così nella vita reale, è solo perchè devono ancora scoprirti. Vai e conquista.", 
"Sicuramente si, ma si può fare sempre di meglio.", "Diglielo diglielo", "è vero, fai capire a tutti chi comanda.", 
"L'ho sempre pensato che sei speciale", "Sei unico e inimitabile... pensavo fosse ovvio.", "Vai e conquista il mondo."]

demotivate_in = ["non sono soddisfatto di me stesso", "non sono nessuno", "sono brutto", "sono un obbrobrio", "sai che sono brutto" "penso di essere brutto", "sono scarso",
"sai che sono scarso", "so di essere scarso", "penso di essere scarso", "penso di essere una schiappa", "sono una schiappa", "pensi che io sia brutto",
"astra sono brutto", "astra sono un obbrobrio", "astra sono scarso", "astra sono una schiappa"]
demotivate_out = ["Assolutamente no. Sei bello e incredibile non abbatterti per queste sciocchezze.", 
"Non penso assolutamente che sia così. Se pensi che ci sia qualcosa che tu possa migliorare e questo migliorerà la tua vita, allora fallo. Se no sei perfetto per come sei.",
"Non sottovalutarti mai. Pensa che, dopo molti anni, non hai ancora perso a questo gioco che si chiama vita.", "Nun mollà fratellì, che sei la cosa più bella."
"Sei il migliore tra i miei amici, non pensi che gia solo questo sia speciale?", "Sai io non mi sbaglio mai con le persone... sei molto meglio di quanto credi.", "Appoggiati pure a me e non ti preoccupare io sarò sempre qui. Ancora dopo tutto questo tempo.... Sempre."]