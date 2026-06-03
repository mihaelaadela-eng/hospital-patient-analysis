# PROIECT 1 - Patient Triage System
# Mihaela Adela Tepes Grosu
# Healthcare AI - Python Learning

# Lista de pacienti
pacienti = [
    {"nume": "John Smith", "varsta": 45, "temperatura": 38.5, "hemoglobina": 10.5},
    {"nume": "Maria Garcia", "varsta": 32, "temperatura": 36.8, "hemoglobina": 13.2},
     {"nume": "David Lee", "varsta": 67, "temperatura": 39.2, "hemoglobina": 8.1},
     {"nume": "Anna Brown", "varsta": 28, "temperatura": 36.5, "hemoglobina": 14.0},
      {"nume": "James Wilson", "varsta": 55, "temperatura": 37.1, "hemoglobina": 7.5},
]

# Functie de triage
def triage_pacient(pacient):
    urgenta= False
    probleme = []

    if pacient["temperatura"] > 38.0:
        probleme.append("FEBRA: " + str(pacient["temperatura"]))
        urgenta = True
    if pacient["hemoglobina"] < 9.0:
            probleme.append("HEMOGLOBINA CRITICA: " + str(pacient["hemoglobina"]))
            urgenta = True
    return urgenta, probleme

# Raport final
print("=== PATIENT TRIAGE SYSTEM ===")
print("Total pacienti:", len(pacienti))
print("---")

urgenti = []

for pacient in pacienti:
    urgenta, probleme = triage_pacient(pacient)
    if urgenta:
        urgenti.append(pacient["nume"])
        print("URGENT:", pacient["nume"])
        for problema in probleme:
            print("  ->", problema)
        print("---")
        
print("SUMAR URGENTE:", len(urgenti) , "pacienti necesita atentie")
print("Pacienti urgenti:", urgenti)