import pandas as pd
import matplotlib.pyplot as plt

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

# GRAFIC 1 — Costuri per diagnostic
costuri = df.groupby('diagnostic')['cost_internare_GBP'].sum()

plt.figure(figsize=(8, 5))
costuri.plot(kind='bar', color=['#2196F3', '#4CAF50', '#FF5722'])
plt.title('Cost Total per Diagnostic')
plt.xlabel('Diagnostic')
plt.ylabel('Cost (GBP)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('grafic_costuri.png')
plt.show()
print("=== Grafic 1 salvat! ===")

# GRAFIC 2 — Distributie diagnostice (pie chart)
diagnostice = df['diagnostic'].value_counts()

plt.figure(figsize=(6, 6))
diagnostice.plot(kind='pie', autopct='%1.1f%%', 
                 colors=['#2196F3', '#4CAF50', '#FF5722'])
plt.title('Distributie Pacienti per Diagnostic')
plt.ylabel('')
plt.tight_layout()
plt.savefig('grafic_distributie.png')
plt.show()
print("=== Grafic 2 salvat! ===")