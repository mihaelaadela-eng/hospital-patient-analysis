import pandas as pd

data = {
    'nume': ['Ana Ionescu', 'Ion Pop', 'Maria Rus', 'Petre Dima', 
             'Elena Stoica', 'Gheorghe Marin', 'Ioana Vlad', 'Mihai Constantin'],
    'varsta': [67, 45, 72, 38, 55, 81, 63, 49],
    'diagnostic': ['hipertensiune', 'diabet', 'hipertensiune', 'anxietate',
                   'hipertensiune', 'diabet', 'hipertensiune', 'diabet'],
    'tensiune': [145, 120, 160, 118, 155, 122, 148, 119],
    'zile_internare': [3, 5, 7, 2, 4, 10, 6, 3]
}

df = pd.DataFrame(data)

df['cost_internare_GBP'] = df['zile_internare'] * 200

print("=== Tabel cu costuri ===")
print(df)

print("\n=== Cost total per diagnostic ===")
print(df.groupby('diagnostic')['cost_internare_GBP'].sum())

print("\n=== Pacientul cu cele mai multe zile ===")
print(df[df['zile_internare'] == df['zile_internare'].max()])

df.to_excel('raport_pacienti.xlsx', index=False)
print("\n=== Fisierul Excel a fost salvat! ===")