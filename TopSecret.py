print("SCEMO CHI LEGGE!")

import time
import sys

def animate():
    for i in range(20):
        sys.stdout.write("\r" + "SUC" + "A" * (i % 10))
        sys.stdout.flush()
        time.sleep(0.2)

animate()

import random

soggetti = ["Il gatto", "La luna", "Il vento", "Un elefante", "Una nuvola"]
verbi = ["balla", "scivola", "sussurra", "corre", "canta"]
completamenti = ["sotto il cielo", "sopra le montagne", "nella notte oscura", "tra le stelle"]

poesia = f"{random.choice(soggetti)} {random.choice(verbi)} {random.choice(completamenti)}."
print(poesia)

from datetime import datetime

data_speciale = input("Inserisci una data speciale per te  (gg/mm/aaaa): ")
data_speciale= datetime.strptime(data_speciale, "%d/%m/%Y")
oggi = datetime.now()

differenza = oggi - data_speciale
print(f"Morirai tra {differenza.days} giorni!")