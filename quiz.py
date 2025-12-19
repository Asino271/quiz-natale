import os
import time

# Colori ANSI
ROSSO = "\033[91m"
VERDE = "\033[92m"
GIALLO = "\033[93m"
BLU = "\033[94m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def intro_natale():
    clear()
    print(ROSSO + "🎄🎅🎁 BUON NATALE! 🎁🎅🎄" + RESET) 
    print(VERDE + """
          *
         /_\\
        /* *\\
       /*   *\\
      /*******\\
         || 
         ||
    """ + RESET)
    time.sleep(2)
    input(f"Babbo Natale Tecnologico ha creato un biglietto non Analogico\n"
          "se il regalo vuoi indovinare, le risposte giuste devi trovare\n"

          "Premi INVIO per iniziare il quiz di Babbo Natale 🎄")

def quiz():
    domande = [
        {
            "domanda": "Per il regalo di quest'anno, tocca viaggiare\n"
                        "e in tutta onestà conviene darsi una mossa\n"
                        "sicché se davvero vuoi andare dobbiamo prenotare un...",
            "risposta": "frecciarossa"
        },
        {
            "domanda": "Frecciarossa, si, ma dove andiamo?\n"
                        "Vabbeh è semplice, solo al cibo noi pensiamo\n"
                        "sicché presto prenotiamo una cena al...",
            "risposta": "rifugio romano"
        },
        {
            "domanda": "Certo è cruciale capire in che mese\n"
                        "perché dopo mangiato tocca una passeggiata a...",
            "risposta": "villa borghese"
        },
        {
            "domanda": "Ormai avrai capito che il regalo di Babbo\n"
                        "E' far la vita da nababbo\n"
                        "Viaggio, Cena, Alloggio e visita policroma\n"
                        "il regalo è un weekend a...",
            "risposta": "roma"
        }
    ]

    for i, d in enumerate(domande, start=1):
        while True:
            risposta = input(
                BLU + f"\n🎁 Domanda {i}: {d['domanda']}" + RESET
            ).strip().lower()

            if risposta == d["risposta"]:
                print(VERDE + "🎄 Risposta corretta!" + RESET)
                break
            else:
                print(ROSSO + "❄️ Risposta sbagliata, riprova!" + RESET)

    print(VERDE + "\n🎉🎁 Hai sbloccato il regalo di Natale 2025! 🎁🎉\n" "Ti Amo 🤍 " + RESET)
    input("\nPremi INVIO per uscire...")

if __name__ == "__main__":
    intro_natale()
    quiz()
