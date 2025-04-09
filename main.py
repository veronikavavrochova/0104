import random

barvy = ["červená", "modrá", "žlutá"]
barvy.append("fialová")
nahodna_barva = random.choice(barvy)
print(nahodna_barva)
    
   
polozky = ["kabát", "chleba", "bicykl", "sýr","automobil"]
for i in range(10):
    osoba1_volba = random.choice(polozky)
    osoba2_volba = random.choice(polozky)
    
    
print (f"kupme{osoba1_volba}.")
print (f"Ne, kupme{osoba1_volba}.")
if osoba1_volba == osoba2_volba:
    