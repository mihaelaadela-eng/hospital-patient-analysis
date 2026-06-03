import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# DATE
# ============================================

pacienti = pd.DataFrame({
    'id_pacient': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nume': ['Ana Ionescu', 'Ion Pop', 'Maria Rus', 'Petre Dima',
             'Elena Stoica', 'Gheorghe Marin', 'Ioana Vlad', 'Mihai Constantin',
             'Rodica Popa', 'Vasile Dumitrescu'],
    'varsta': [67, 45, 72, 38, 55, 81, 63, 49, 70, 58],
    'id_sectie': [1, 2, 1, 3, 1, 2, 1, 2, 1, 3],
    'zile_internare': [3, 5, 7, 2, 4, 10, 6, 3, 8, 4],
    'readmis': ['Nu', 'Nu', 'Da', 'Nu', 'Da', 'Nu', 'Da', 'Nu', 'Nu', 'Da']
})

sectii = pd.DataFrame({
    'id_sectie': [1, 2, 3],
    'nume_sectie': ['Cardiologie', 'Diabet', 'Psihiatrie'],
    'cost_zi_GBP': [300, 250, 200]
})

# ============================================
# ANALIZA
# ============================================

df = pd.merge(pacienti, sectii, on='id_sectie', how='left')
df['cost_total_GBP'] = df['zile_internare'] * df['cost_zi_GBP']

print("=== RAPORT COMPLET SPITAL ===")
print(df[['nume', 'varsta', 'nume_sectie', 'zile_internare', 'cost_total_GBP', 'readmis']])

print("\n=== Cost total per sectie ===")
costuri_sectie = df.groupby('nume_sectie')['cost_total_GBP'].sum()
print(costuri_sectie)

print("\n=== Pacienti readmisi ===")
print(df[df['readmis'] == 'Da'][['nume', 'nume_sectie', 'cost_total_GBP']])

print("\n=== Cost mediu per sectie ===")
print(df.groupby('nume_sectie')['cost_total_GBP'].mean().round(0))

# ============================================
# GRAFICE
# ============================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Hospital Patient Analysis', fontsize=14, fontweight='bold')

# Grafic 1 - Cost total per sectie
costuri_sectie.plot(kind='bar', ax=axes[0], 
                    color=['#2196F3', '#4CAF50', '#FF5722'])
axes[0].set_title('Cost Total per Sectie')
axes[0].set_xlabel('Sectie')
axes[0].set_ylabel('Cost (GBP)')
axes[0].tick_params(axis='x', rotation=0)

# Grafic 2 - Zile internare per pacient
df.plot(kind='bar', x='nume', y='zile_internare', 
        ax=axes[1], color='#9C27B0', legend=False)
axes[1].set_title('Zile Internare per Pacient')
axes[1].set_xlabel('Pacient')
axes[1].set_ylabel('Zile')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('raport_spital.png')
plt.show()

# ============================================
# EXPORT
# ============================================

df.to_excel('raport_spital.xlsx', index=False)
print("\n=== Raport salvat: raport_spital.xlsx + raport_spital.png ===")