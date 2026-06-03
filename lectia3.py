# Lectia 3 - Conditii (if/else)
# Cum ia Python decizii - ca tine in clinica

temperatura = 36.8

if temperatura > 38.0:
    print("ALERT: Pacient are febra!")
    print("Temperatura:", temperatura)
else:
    print("Temperatura normala:", temperatura)

# Alt exemplu - rezultat laborator 
hemoglobina = 10.5

if hemoglobina < 12.0:
    print ("ALERT: Hemoglobina scazuta - actiune necesara")
elif hemoglobina > 17.0:
    print("ALERT: Hemoglobina ridicata - investigatie necesara")
else:
    print("Hemoglobina in limite normale:", hemoglobina)