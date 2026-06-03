# Lectia 6 - Functii
# Cum cream blocuri de cod reutilizabile

# 0 functie simpla
def verifica_temperatura(nume, temp):
    print("Pacient:", nume)
    if temp > 38.0:
        print("STATUS: FEBRA -",temp)
    elif temp < 36.0:
        print("STATUS: HIPOTERMIE -", temp)
    else:
        print("STATUS: Normal -", temp)
        print("===")
# Folosim functia pentru mai multi pacienti
verifica_temperatura("John Smith", 36.8)
verifica_temperatura("Maria Garcia", 38.5)
verifica_temperatura("David Lee", 35.5)
verifica_temperatura("Ann Brown", 39.1)