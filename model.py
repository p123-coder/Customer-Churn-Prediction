import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 1. Load dataset
data = pd.read_csv("data/Telco-Customer-Churn.csv")

print("Dataset loaded successfully!")
print("Total customers:", len(data))


# 2. Convert TotalCharges to numeric
data["TotalCharges"] = pd.to_numeric(
    data["TotalCharges"],
    errors="coerce"
)


# 3. Remove rows with missing values
data = data.dropna()


# 4. Remove customer ID
data = data.drop("customerID", axis=1)


# 5. Convert target variable
data["Churn"] = data["Churn"].map({
    "No": 0,
    "Yes": 1
})


# 6. Separate input and target
X = data.drop("Churn", axis=1)
y = data["Churn"]


# 7. Identify categorical and numerical columns
categorical_columns = X.select_dtypes(
    include=["object"]
).columns

numerical_columns = X.select_dtypes(
    exclude=["object"]
).columns


# 8. Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        ),
        (
            "numerical",
            "passthrough",
            numerical_columns
        )
    ]
)


# 9. Create Machine Learning model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])


# 10. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 11. Train model
print("\nTraining model...")
model.fit(X_train, y_train)


# 12. Make predictions
y_pred = model.predict(X_test)


# 13. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Training Completed!")
print(f"Accuracy: {accuracy * 100:.2f}%")


# 14. Classification report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["No Churn", "Churn"]
    )
)


# 15. Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# 16. Test with sample customers
sample_data = X_test.head(5)

sample_predictions = model.predict(sample_data)

print("\nSample Predictions:")

for prediction in sample_predictions:
    if prediction == 1:
        print("Customer may CHURN")
    else:
        print("Customer may NOT CHURN")