import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# ============================================
# DATE — 100 pacienti
# ============================================

np.random.seed(42)
n = 100

df = pd.DataFrame({
    'varsta': np.random.randint(40, 85, n),
    'colesterol': np.random.randint(150, 280, n),
    'greutate': np.random.randint(55, 110, n)
})

# Tensiunea depinde de varsta + colesterol + zgomot
df['tensiune'] = (
    0.5 * df['varsta'] +
    0.2 * df['colesterol'] +
    0.1 * df['greutate'] +
    np.random.randint(-10, 10, n)
)

print("=== DATE PACIENTI ===")
print(df.head())

# ============================================
# MACHINE LEARNING
# ============================================

# X = ce stim despre pacient
# y = ce vrem sa prezicam
X = df[['varsta', 'colesterol', 'greutate']]
y = df['tensiune']

# Impartim datele: 80% antrenare, 20% testare
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\n=== DATE ANTRENARE / TESTARE ===")
print(f"Antrenare: {len(X_train)} pacienti")
print(f"Testare:   {len(X_test)} pacienti")

# Antrenam modelul
model = LinearRegression()
model.fit(X_train, y_train)

# Prezicam
y_pred = model.predict(X_test)

# ============================================
# REZULTATE
# ============================================

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n=== PERFORMANTA MODEL ===")
print(f"Eroare medie: {mae:.1f} mmHg")
print(f"Acuratete R2: {r2:.2f} (1.0 = perfect)")

# Prezicere pentru un pacient nou
pacient_nou = pd.DataFrame({
    'varsta': [65],
    'colesterol': [240],
    'greutate': [85]
})

tensiune_prezisa = model.predict(pacient_nou)
print(f"\n=== PREZICERE PACIENT NOU ===")
print(f"Varsta: 65, Colesterol: 240, Greutate: 85 kg")
print(f"Tensiune prezisa: {tensiune_prezisa[0]:.1f} mmHg")

# ============================================
# GRAFIC
# ============================================

plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, color='#2196F3', alpha=0.7)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         'r--', linewidth=2, label='Predictie perfecta')
plt.xlabel('Tensiune Reala')
plt.ylabel('Tensiune Prezisa')
plt.title('Model ML — Tensiune Reala vs Prezisa')
plt.legend()
plt.tight_layout()
plt.savefig('ml_rezultate.png')
plt.show()

print("\n=== Model salvat! ===")