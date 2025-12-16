import numpy as np
import pandas as pd

np.random.seed(42)
n = 1000

df = pd.DataFrame({
    "age": np.random.randint(18, 80, n),
    "gender": np.random.choice(["M", "F"], n),
    "temp": np.random.normal(37, 0.8, n),
    "sys_bp": np.random.normal(125, 15, n),
    "dia_bp": np.random.normal(80, 10, n),
    "spo2": np.random.normal(97, 2, n),
    "hr": np.random.normal(85, 12, n),
    "fever": np.random.binomial(1, 0.3, n),
    "cough": np.random.binomial(1, 0.4, n),
    "fatigue": np.random.binomial(1, 0.5, n),
    "chest_pain": np.random.binomial(1, 0.2, n),
    "sob": np.random.binomial(1, 0.25, n),
})

df["label"] = np.where(
    (df["fever"] == 1) & (df["cough"] == 1), "flu",
    np.where(df["chest_pain"] == 1, "heart_issue", "normal")
)

df.to_csv("dataset.csv", index=False)
