import pandas as pd

# Tabel principal - pacienti
pacienti = pd.DataFrame({
    'id_pacient': [1, 2, 3, 4, 5, 6, 7, 8],
    'nume': ['Ana Ionescu', 'Ion Pop', 'Maria Rus', 'Petre Dima',
             'Elena Stoica', 'Gheorghe Marin', 'Ioana Vlad', 'Mihai Constantin'],
    'varsta': [67, 45, 72, 38, 55, 81, 63, 49],
    'id_sectie': [1, 2, 1, 3, 1, 2, 1, 2],
    'zile_internare': [3, 5, 7, 2, 4, 10, 6, 3]
})

# Al doilea tabel - sectii
sectii = pd.DataFrame({
    'id_sectie': [1, 2, 3],
    'nume_sectie': ['Cardiologie', 'Diabet', 'Psihiatrie'],
    'cost_zi_GBP': [300, 250, 200]
})

print("=== Tabel Pacienti ===")
print(pacienti)

print("\n=== Tabel Sectii ===")
print(sectii)

# MERGE — combinam cele doua tabele
df = pd.merge(pacienti, sectii, on='id_sectie', how='left')

print("\n=== Tabel Combinat ===")
print(df)

# Calculam costul real per pacient
df['cost_total_GBP'] = df['zile_internare'] * df['cost_zi_GBP']

print("\n=== Cu costuri reale ===")
print(df[['nume', 'nume_sectie', 'zile_internare', 'cost_total_GBP']])

# GROUPBY — total costuri per sectie
print("\n=== Cost total per sectie ===")
print(df.groupby('nume_sectie')['cost_total_GBP'].sum())

# GROUPBY — media zilelor de internare per sectie
print("\n=== Media zile internare per sectie ===")
print(df.groupby('nume_sectie')['zile_internare'].mean().round(1))