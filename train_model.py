import pickle

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load the data we created with generate_data.py
data = pd.read_csv("data/students.csv")

# The 5 columns we'll use to make a prediction
features = ["attendance", "study_hours", "previous_score", "assignment_completion", "participation"]
X = data[features]              # the inputs
y = data["performance"]         # the answer we want to predict

# Step 2: Split the data - most of it for training, some held back for testing.
# This lets us check how well the model does on students it hasn't seen before.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create and train the model.
# max_depth=4 keeps the "flowchart" simple enough to still make sense to a human.
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# Step 4: Check how good it is on the test students
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy on test data: {accuracy * 100:.1f}%")

# Step 5: Save the trained model to a file so app.py can use it later,
# without needing to retrain every time.
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Saved trained model to model.pkl")
