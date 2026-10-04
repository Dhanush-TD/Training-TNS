import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# 1. Linear Regression - Salary Prediction
experience = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
salary = np.array([20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000])

salary_model = LinearRegression()
salary_model.fit(experience, salary)

print("Predicted salary for 5 years:", salary_model.predict([[5]])[0])


# 2. Logistic Regression - Product Purchase
purchase_df = pd.DataFrame({
    "Age": [20, 22, 25, 28, 30, 35, 40, 45],
    "Income": [15000, 18000, 25000, 30000, 35000, 40000, 50000, 60000],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]
})

purchase_model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])
purchase_model.fit(purchase_df[["Age", "Income"]], purchase_df["Purchased"])

new_input = pd.DataFrame({"Age": [32], "Income": [38000]})
result = purchase_model.predict(new_input)[0]
print("Will purchase:", "Yes" if result == 1 else "No")


# 3. Evaluation Metrics - Spam Detection
actual = [1, 1, 1, 0, 0, 0, 1, 0]
predicted = [1, 1, 0, 0, 0, 1, 1, 0]

print("Accuracy:", accuracy_score(actual, predicted))
print("Precision:", precision_score(actual, predicted))
print("Recall:", recall_score(actual, predicted))
print("F1-score:", f1_score(actual, predicted))


# 4. Decision Tree - Play Game
game_df = pd.DataFrame({
    "Weather": ["Sunny", "Sunny", "Rainy", "Rainy", "Cloudy", "Cloudy", "Sunny", "Rainy"],
    "Temperature": ["Hot", "Cool", "Cool", "Hot", "Hot", "Cool", "Hot", "Cool"],
    "Play": [0, 1, 1, 0, 1, 1, 0, 1]
})

weather_map = {"Sunny": 0, "Rainy": 1, "Cloudy": 2}
temp_map = {"Hot": 0, "Cool": 1}

game_X = pd.DataFrame({
    "Weather": game_df["Weather"].map(weather_map),
    "Temperature": game_df["Temperature"].map(temp_map)
})

game_model = DecisionTreeClassifier(random_state=42)
game_model.fit(game_X, game_df["Play"])

new_day = pd.DataFrame({"Weather": [weather_map["Sunny"]], "Temperature": [temp_map["Cool"]]})
print("Play:", "Yes" if game_model.predict(new_day)[0] == 1 else "No")


# 5. Random Forest - Customer Churn
churn_df = pd.DataFrame({
    "Age": [22, 25, 30, 35, 40, 28, 45, 32],
    "Tenure": [2, 5, 1, 8, 10, 3, 12, 2],
    "Monthly Bill": [500, 600, 800, 550, 500, 900, 650, 850],
    "Churn": [1, 0, 1, 0, 0, 1, 0, 1]
})

churn_model = RandomForestClassifier(n_estimators=100, random_state=42)
churn_model.fit(churn_df[["Age", "Tenure", "Monthly Bill"]], churn_df["Churn"])

new_customer = pd.DataFrame({"Age": [29], "Tenure": [2], "Monthly Bill": [750]})
print("Customer will:", "Leave" if churn_model.predict(new_customer)[0] == 1 else "Stay")


# Problem Statement: Customer Purchase Prediction
data = pd.DataFrame({
    "Age": [20, 22, 25, 28, 30, 32, 35, 38, 40, 45],
    "Income": [15000, 18000, 22000, 30000, 35000, 40000, 45000, 50000, 55000, 60000],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
})

X = data[["Age", "Income"]]
y = data["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

log_model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])
log_model.fit(X_train, y_train)

tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

new_customer = pd.DataFrame({"Age": [27], "Income": [28000]})

log_pred = log_model.predict(new_customer)[0]
tree_pred = tree_model.predict(new_customer)[0]

print("Logistic Regression ->", "Purchase" if log_pred == 1 else "No purchase")
print("Decision Tree ->", "Purchase" if tree_pred == 1 else "No purchase")

log_accuracy = accuracy_score(y_test, log_model.predict(X_test))
tree_accuracy = accuracy_score(y_test, tree_model.predict(X_test))

print("Accuracy of Logistic Regression:", log_accuracy)
print("Accuracy of Decision Tree:", tree_accuracy)