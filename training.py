import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
import pickle

# Load dataset
df = pd.read_csv("adtech_5M_dataset.csv")

print("Dataset Loaded:")
print(df.shape)

# Target
y = df["installed"]

# Features
X = df.drop(["installed"], axis=1)

# Convert text columns
X = pd.get_dummies(X)

print("Preparing Train/Test Split...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

print("Training Model...")

model = XGBClassifier(

    n_estimators=600,
    max_depth=14,
    learning_rate=0.03,

    subsample=0.9,
    colsample_bytree=0.9,

    min_child_weight=1,

    gamma=0.1,

    tree_method="hist",

    eval_metric="auc"
)
model.fit(X_train, y_train)

print("Model Trained")

# Predictions
pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:,1]

print("Accuracy:", accuracy_score(y_test, pred))
print("AUC Score:", roc_auc_score(y_test, prob))

print("\nClassification Report:")
print(classification_report(y_test, pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))

print("\nInstall Rate:", y.mean())

# Save model
pickle.dump(model, open("adtech_model.pkl","wb"))
# Save training columns
pickle.dump(X.columns, open("training_columns.pkl","wb"))

print("Model Saved Successfully")