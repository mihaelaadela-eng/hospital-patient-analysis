# Lectia 4 - Liste
# In nursng lucram cu liste de pacienti, medicamente etc

# Lista de pacienti
pacienti = ["John Smith", "Maria Garcia", "David Lee", "Ann Brown"]

# Lista de temperaturi
temperaturi = [36.8, 38.5, 37.3, 39.1]

# Afisam lista 
print("=== LISTA PACIENTI ===")
print(pacienti)

# Accesam un pacint specific
print("Primul pacient:", pacienti[0])
print("Al doilea pacient:", pacienti[1])

#Cati pacienti avem
print("Total pacienti:", len(pacienti))

# Adaugam un pacient nou
pacienti.append("James Wilson")
print("Dupa adaugare:", pacienti)
print("Total acum:", len(pacienti))