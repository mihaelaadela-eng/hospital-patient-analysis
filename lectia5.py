# Lectia 5 - Bucle (loops)
# Cum repetam actiuni automat - esential in AI si data

# Lista pacienti cu temperaturi
pacienti = ["John SMith", "Maria Garcia", "David Lee", "Anna Brown",]
temperaturi = [36.8, 38.5, 37.2, 39.1]
# Verificam fiecare pacient automat
print("=== VERIFICARE TEMPERATURI ===")

for i in range(len(pacienti)):
    print("---")
    print("Pacient:", pacienti[i])
    print("Tempertura:", temperaturi[i])
    if temperaturi[i] > 38.0:
        print("STATUS: FEBRA _ actiune necesara!")
else:   
            print("STATUS : Normal")

print("---")
print("Verificarea completa pentru", len(pacienti), "pacienti")