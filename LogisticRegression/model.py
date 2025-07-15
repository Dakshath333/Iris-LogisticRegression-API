from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pickle

# Load dataset
X, y = load_iris(return_X_y=True)

# Build pipeline: scaler + model
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))

# Train the model
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)


