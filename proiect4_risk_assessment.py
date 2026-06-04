import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# DATE — 50 pacienti
# ============================================

np.random.seed(42)
n = 50

df = pd.DataFrame({
    'id': range(1, n+1),
    'varsta': np.random.randint(40, 85, n),
    'tensiune': np.random.randint(110, 180, n),
    'colesterol': np.random.randint(150, 280, n),
    'diabet': np.random.choice(['Da', 'Nu'], n, p=[0.3, 0.7]),
    'fumat': np.random.choice(['Da', 'Nu'], n, p=[0.25, 0.75]),
    'zile_internare': np.random.randint(1, 15, n)
})

# ============================================
# SCOR RISC
# ============================================

def calculeaza_risc(row):
    scor = 0
    if row['tensiune'] > 160: scor += 3
    elif row['tensiune'] > 140: scor += 2
    else: scor += 1
    if row['colesterol'] > 240: scor += 3
    elif row['colesterol'] > 200: scor += 2
    else: scor += 1
    if row['varsta'] > 70: scor += 3
    elif row['varsta'] > 55: scor += 2
    else: scor += 1
    if row['diabet'] == 'Da': scor += 2
    if row['fumat'] == 'Da': scor += 2
    return scor

df['scor_risc'] = df.apply(calculeaza_risc, axis=1)

def categorie_risc(scor):
    if scor >= 10: return 'Risc Inalt'
    elif scor >= 7: return 'Risc Mediu'
    else: return 'Risc Scazut'

df['categorie'] = df['scor_risc'].apply(categorie_risc)

# ============================================
# RAPORT
# ============================================

print("=== PATIENT RISK ASSESSMENT REPORT ===")
print(f"\nTotal pacienti: {n}")
print("\n=== Distributie risc ===")
print(df['categorie'].value_counts())

print("\n=== Statistici per categorie ===")
print(df.groupby('categorie')[['varsta', 'tensiune', 'colesterol']].mean().round(1))

print("\n=== Top 5 pacienti risc inalt ===")
top5 = df[df['categorie'] == 'Risc Inalt'].nlargest(5, 'scor_risc')
print(top5[['id', 'varsta', 'tensiune', 'colesterol', 'diabet', 'fumat', 'scor_risc']])

# ============================================
# GRAFICE
# ============================================

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Patient Risk Assessment Report', fontsize=14, fontweight='bold')

culori = {'Risc Scazut': '#4CAF50', 'Risc Mediu': '#FF9800', 'Risc Inalt': '#F44336'}

# Grafic 1 — Distributie categorii
categorii = df['categorie'].value_counts()
categorii.plot(kind='bar', ax=axes[0,0],
               color=[culori[c] for c in categorii.index])
axes[0,0].set_title('Distributie Risc')
axes[0,0].tick_params(axis='x', rotation=0)

# Grafic 2 — Scor risc histogram
axes[0,1].hist(df['scor_risc'], bins=8, color='#2196F3', edgecolor='white')
axes[0,1].set_title('Distributie Scor Risc')
axes[0,1].axvline(x=7, color='orange', linestyle='--', label='Risc Mediu')
axes[0,1].axvline(x=10, color='red', linestyle='--', label='Risc Inalt')
axes[0,1].legend()

# Grafic 3 — Varsta vs Tensiune
colors = df['categorie'].map(culori)
axes[1,0].scatter(df['varsta'], df['tensiune'], c=colors, alpha=0.7)
axes[1,0].set_title('Varsta vs Tensiune')
axes[1,0].set_xlabel('Varsta')
axes[1,0].set_ylabel('Tensiune')

# Grafic 4 — Media tensiune per categorie
df.groupby('categorie')['tensiune'].mean().plot(
    kind='bar', ax=axes[1,1],
    color=[culori[c] for c in df.groupby('categorie')['tensiune'].mean().index])
axes[1,1].set_title('Tensiune Medie per Categorie')
axes[1,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig('risk_assessment.png')
plt.show()

# ============================================
# EXPORT
# ============================================

df.to_excel('risk_assessment.xlsx', index=False)
print("\n=== Raport salvat: risk_assessment.xlsx + risk_assessment.png ===")