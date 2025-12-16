import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1) Load data
df = pd.read_csv("dataset.csv")

# 2) Separate X/y
y = df["label"]
X = df.drop(columns=["label"])

# 3) Column types
numeric_cols = ["age", "temp", "sys_bp", "dia_bp", "spo2", "hr",
                "fever", "cough", "fatigue", "chest_pain", "sob"]
categorical_cols = ["gender"]  # optional

# 4) Preprocessing
preprocess = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ],
    remainder="drop",
)

# 5) Models
logreg = LogisticRegression(max_iter=2000, class_weight="balanced")
rf = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced_subsample",
    n_jobs=-1
)

# 6) Pipelines
logreg_pipe = Pipeline(steps=[("prep", preprocess), ("model", logreg)])
rf_pipe = Pipeline(steps=[("prep", preprocess), ("model", rf)])

# 7) Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 8) Train
logreg_pipe.fit(X_train, y_train)
rf_pipe.fit(X_train, y_train)

# 9) Evaluate
print("Logistic Regression:\n", classification_report(y_test, logreg_pipe.predict(X_test)))
print("Random Forest:\n", classification_report(y_test, rf_pipe.predict(X_test)))

# 10) Save models
joblib.dump(logreg_pipe, "logreg_model.joblib")
joblib.dump(rf_pipe, "rf_model.joblib")

print("✅ Saved: logreg_model.joblib and rf_model.joblib")
