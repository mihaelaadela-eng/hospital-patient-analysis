# Lectia 7 - Dictionare
# Cum stocam date structurate - ca o fisa de pacient complata

# Un dictionar = fisa pacient 
pacient = {
    "nume":"John Smith",
    "varsta": 45,
    "diagnostic": "Post-op Urology",
    "temperatura": 38.5,
    "alergic": False
}

# Accesam date din dictionar 
print("=== FISA PACTIENT ===")
print("Nume:", pacient["nume"])
print("Varsta:", pacient["varsta"])
print("Diagnostic:", pacient["diagnostic"])
print("Temperatura:", pacient["temperatura"])
print("Alergic:", pacient["alergic"])

# Modificam o valoare
pacient["temperatura"] = 37.2
print("Temperatura actualizata:", pacient["temperatura"])

# Adaugam un camp nou
pacient["salon"] = "3B"
print("Salon:", pacient["salon"])