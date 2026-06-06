import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ============================================
# DATE — 200 pacienti
# ============================================

np.random.seed(42)
n = 200

df = pd.DataFrame({
    'varsta': np.random.randint(40, 85, n),
    'tensiune': np.random.randint(110, 180, n),
    'colesterol': np.random.randint(150, 280, n),
    'zile_internare': np.random.randint(1, 15, n),
    'diabet': np.random.randint(0, 2, n),
    'fumat': np.random.randint(0, 2, n)
})

# Readmis = 1 daca risc inalt
df['readmis'] = (
    (df['varsta'] > 65).astype(int) +
    (df['tensiune'] > 150).astype(int) +
    (df['colesterol'] > 230).astype(int) +
    (df['zile_internare'] > 7).astype(int) +
    df['diabet'] +
    df['fumat']
)
df['readmis'] = (df['readmis'] >= 3).astype(int)

print("=== DATE PACIENTI ===")
print(f"Total pacienti: {n}")
print(f"Readmisi: {df['readmis'].sum()} ({df['readmis'].mean()*100:.1f}%)")

# ============================================
# MACHINE LEARNING
# ============================================

X = df[['varsta', 'tensiune', 'colesterol',
        'zile_internare', 'diabet', 'fumat']]
y = df['readmis']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest — algoritm foarte folosit in Healthcare AI
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# ============================================
# REZULTATE
# ============================================

acuratete = accuracy_score(y_test, y_pred)
print(f"\n=== PERFORMANTA MODEL ===")
print(f"Acuratete: {acuratete*100:.1f}%")
print(f"\n=== RAPORT DETALIAT ===")
print(classification_report(y_test, y_pred,
      target_names=['Nu readmis', 'Readmis']))

# Importanta factorilor
importanta = pd.DataFrame({
    'factor': X.columns,
    'importanta': model.feature_importances_
}).sort_values('importanta', ascending=False)

print("\n=== CE FACTORI CONTEAZA CEL MAI MULT? ===")
print(importanta)

# ============================================
# PREZICERE PACIENT NOU
# ============================================

pacient_nou = pd.DataFrame({
    'varsta': [72],
    'tensiune': [165],
    'colesterol': [250],
    'zile_internare': [9],
    'diabet': [1],
    'fumat': [0]
})

predictie = model.predict(pacient_nou)
probabilitate = model.predict_proba(pacient_nou)

print(f"\n=== PREZICERE PACIENT NOU ===")
print(f"Varsta: 72, Tensiune: 165, Colesterol: 250")
print(f"Zile internare: 9, Diabet: Da, Fumat: Nu")
print(f"Predictie: {'READMIS' if predictie[0] == 1 else 'NU READMIS'}")
print(f"Probabilitate readmitere: {probabilitate[0][1]*100:.1f}%")

# ============================================
# GRAFIC
# ============================================

plt.figure(figsize=(8, 5))
plt.barh(importanta['factor'], importanta['importanta'],
         color='#2196F3')
plt.title('Factori care prezic readmiterea')
plt.xlabel('Importanta')
plt.tight_layout()
plt.savefig('ml_classification.png')
plt.show()

print("\n=== Model salvat! ===")