# Linear Regression
from sklearn.linear_model import LinearRegression

import numpy as np

x = np.array([[1], [2], [3], [4], [5]])

y = np.array([20, 30, 40, 50, 60])

model = LinearRegression()

model.fit(x, y)

prediction = model.predict([[8]])

print(prediction)


# Logistic Regression Example
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6], [7], [8]]

y = [0, 0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[4.5]])

print("Prediction:", prediction)

if prediction == 1:
    print("Student will Pass")
else:
    print("Student will Fail")


# Evaluation Metrics - Fraud Detection
from sklearn.metrics import classification_report, confusion_matrix

y_true = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
y_pred = [0, 0, 0, 1, 0, 1, 1, 1, 1, 1]

print(confusion_matrix(y_true, y_pred))

print(classification_report(y_true, y_pred, target_names=['Normal', 'Fraud']))


# Decision Trees & Random Forests - Loan Eligibility
from sklearn.ensemble import RandomForestClassifier

X = [[50, 600, 25], [120, 750, 40], [30, 550, 22], [90, 700, 35]]
y = [0, 1, 0, 1]

rf = RandomForestClassifier(n_estimators=10, random_state=42)
rf.fit(X, y)

print(rf.predict([[85, 680, 30]]))


# Support Vector Machines / Classification
from sklearn.svm import SVC

X = [[1, 20], [2, 35], [8, 85], [9, 90]]
y = [0, 0, 1, 1]

svm = SVC(kernel='rbf')
svm.fit(X, y)

print(svm.predict([[6, 75]]))
print(svm.predict([[5, 65]]))
print(svm.predict([[4, 50]]))


# Combined Supervised Learning Algorithm Program - Assignment
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error

np.random.seed(42)
n_samples = 150

df = pd.DataFrame({
    'Distance_KM': np.random.uniform(1.0, 20.0, n_samples),
    'Driver_Exp_Yrs': np.random.uniform(0.5, 10.0, n_samples),
    'Traffic_Density_Score': np.random.uniform(1.0, 10.0, n_samples)
})

df['Delivery_Time_Mins'] = (
    (df['Distance_KM'] * 2.5)
    + (df['Traffic_Density_Score'] * 3.0)
    - (df['Driver_Exp_Yrs'] * 1.1)
    + np.random.normal(15, 3, n_samples)
)

df['Is_Delayed'] = (df['Delivery_Time_Mins'] > 45).astype(int)

X = df[['Distance_KM', 'Driver_Exp_Yrs', 'Traffic_Density_Score']]
X_tr, X_te, y_cls_tr, y_cls_te, y_reg_tr, y_reg_te = train_test_split(
    X, df['Is_Delayed'], df['Delivery_Time_Mins'], test_size=0.2, random_state=42
)

clf_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])
clf_pipeline.fit(X_tr, y_cls_tr)
cls_preds = clf_pipeline.predict(X_te)
print(f"Delay Prediction Accuracy: {accuracy_score(y_cls_te, cls_preds):.2%}")

reg_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
reg_pipeline.fit(X_tr, y_reg_tr)
reg_preds = reg_pipeline.predict(X_te)
rmse = np.sqrt(mean_squared_error(y_reg_te, reg_preds))
print(f"Delivery Time Root Mean Squared Error (RMSE): {rmse:.2f} Mins")