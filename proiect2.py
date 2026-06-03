import pandas as pd
import matplotlib.pyplot as plt

# Date pacienți - un mic dataset medical
data = {
    "patient_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name": ["Alice", "Bob", "Carol", "David", "Emma",
             "Frank", "Grace", "Henry", "Isla", "Jack"],
    "age": [45, 62, 38, 71, 55, 48, 66, 39, 58, 43],
    "gender": ["F", "M", "F", "M", "F", "M", "F", "M", "F", "M"],
    "blood_pressure": [120, 145, 110, 160, 130, 125, 155, 118, 140, 122],
    "heart_rate": [72, 88, 65, 95, 78, 70, 92, 68, 85, 74],
    "glucose": [90, 145, 85, 180, 95, 88, 160, 92, 110, 87]
}

# Cream DataFrame
df = pd.DataFrame(data)

print("=== PATIENT DATASET ===")
print(df)
print(f"\nTotal patients: {len(df)}")