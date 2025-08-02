import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
from sklearn.preprocessing import LabelEncoder

# Fix: Correct __file__ usage
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, 'crop_disease_data.csv')
model_path = os.path.join(BASE_DIR, 'model.pkl')

# Load dataset
df = pd.read_csv(csv_path)

# Features and label
X = df[['symptoms', 'crop']]
y = df['disease']

# Encode each feature column separately
le_symptoms = LabelEncoder()
le_crop = LabelEncoder()

X['symptoms'] = le_symptoms.fit_transform(X['symptoms'])
X['crop'] = le_crop.fit_transform(X['crop'])

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open(model_path, "wb") as f:
    pickle.dump(model, f)
