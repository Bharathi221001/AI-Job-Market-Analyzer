import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
X = data[["Python", "HTML", "CSS", "JavaScript", "Flask", "SQL"]]

# Target
y = data["Role"]

# Encode target labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train model
model = DecisionTreeClassifier()
model.fit(X, y_encoded)

# Save model
joblib.dump(model, "model/model.pkl")
joblib.dump(label_encoder, "model/label_encoder.pkl")

print("Model trained successfully!")