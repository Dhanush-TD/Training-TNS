# Numpy Program
import numpy as np

marks = np.array([[67, 88, 56], [76, 86, 96], [74, 62, 94], [35, 67, 69], [28, 63, 26]])

print("Students Mark")
print(marks)

print("\nAverage of subject-wise")
print(np.mean(marks, axis=0))

print("\nAverage of student-wise")
print(np.mean(marks, axis=1))

print("\nHighest Marks:")
print(np.max(marks))

print("\nLowest Marks:")
print(np.min(marks))

average = np.mean(marks, axis=1)

for i in range(len(average)):
    if average[i] > 70:
        print("Student ", i)


# Pandas
import pandas as pd

datas = {
    "Employee": ["Dharsh", "Kamalesh", "Atish", "Balaji", "Kirupa"],
    "Department": ["IT", "HR", "Sales", "IT", "MD"],
    "Salary": [60000, 55000, 45000, 65000, 70000]
}

df = pd.DataFrame(datas)

print(df)

print("\nIT Deparment Employees")
print(df[df["Department"] == "IT"])

print("\nHighest Salary")
print(df[df["Salary"] == df["Salary"].max()])

print("\n Employee Salary after 10% increment")
df["Updated Salary"] = df["Salary"] * 1.10

print(df)


# Matplotlib (Line, Bar & Scatter)
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 170, 160, 210]

plt.figure(figsize=(6, 4))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.bar(months, sales)
plt.title("Monthly Sales")
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(months, sales)
plt.title("Sales Distribution")
plt.show()


# Seaborn (Heatmap & Pairplot)
import seaborn as sns

tips = sns.load_dataset("tips")

print(tips.head())

correlation = tips.corr(numeric_only=True)

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.show()

sns.pairplot(tips, hue="sex")
plt.show()


# Plotly (Interactive Dashboard)
import plotly.express as px

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 180, 150, 220, 260],
    "Profit": [20, 35, 30, 45, 60]
}

df = pd.DataFrame(data)

fig = px.line(
    df,
    x="Month",
    y=["Sales", "Profit"],
    title="Sales & Profit Dashboard",
    markers=True
)

fig.show()