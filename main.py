skola = ["Matematika" , "Anglictina", "Cestina", "Telak", "Ucp", "Psi"]

print(len(skola))

for predmet in skola:
    print (predmet)

novy_predmet = input ("Zadejte novy predmet: ")

skola.append(novy_predmet)
print(skola)

skola.pop(3)
print(skola)

skola.sort()
print(skola)

skola.reverse()
print(skola)
