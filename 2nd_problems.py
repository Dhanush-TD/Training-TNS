# NumPy - Problem 1: Student Marks Analysis
import numpy as np

marks = np.array([78, 85, 62, 90, 55, 73, 88, 69, 94, 81])

print("Marks:", marks)
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))
print("Marks greater than 75:", marks[marks > 75])


# NumPy - Problem 2: Temperature Analysis
temperatures = np.array([29.5, 31.2, 33.0, 28.4, 30.8, 34.1, 27.9])

print("Temperatures:", temperatures)
print("Average Temperature:", np.mean(temperatures))
print("Highest Temperature:", np.max(temperatures))
print("Lowest Temperature:", np.min(temperatures))

hot_days = np.where(temperatures > 30)[0] + 1
print("Days with temperature above 30:", hot_days)
print("Temperatures on those days:", temperatures[temperatures > 30])

temperatures = temperatures + 2
print("Updated Temperatures:", temperatures)


# Pandas - Problem 3: Student Performance DataFrame
import pandas as pd

students = pd.DataFrame({
    "Name": ["Arun", "Divya", "Karthik", "Meena", "Rahul", "Sneha", "Vijay", "Priya"],
    "Department": ["CSE", "IT", "ECE", "CSE", "MECH", "IT", "EEE", "CSE"],
    "Marks": [82, 68, 91, 74, 55, 88, 63, 79],
    "Attendance": [92, 78, 95, 85, 72, 90, 76, 88]
})

print("First 5 Students:")
print(students.head())

print("\nAverage Marks:", students["Marks"].mean())

print("\nStudents who scored more than 75:")
print(students[students["Marks"] > 75])

print("\nStudents with attendance below 80%:")
print(students[students["Attendance"] < 80])

print("\nStudents sorted by marks:")
print(students.sort_values(by="Marks", ascending=False))


# Pandas - Problem 4: Product Sales Analysis
products = pd.DataFrame({
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"],
    "Category": ["Computers", "Accessories", "Accessories", "Computers", "Audio", "Accessories"],
    "Price": [55000, 500, 1200, 9500, 2500, 3000],
    "Quantity Sold": [15, 120, 80, 30, 55, 45]
})

products["Total Sales"] = products["Price"] * products["Quantity Sold"]
print("Total sales for each product:")
print(products[["Product Name", "Total Sales"]])

top_product = products.loc[products["Total Sales"].idxmax()]
print("\nProduct with highest sales:", top_product["Product Name"], "-", top_product["Total Sales"])

print("\nAverage Product Price:", products["Price"].mean())

print("\nProducts with quantity sold greater than 50:")
print(products[products["Quantity Sold"] > 50])

print("\nProducts sorted by total sales:")
print(products.sort_values(by="Total Sales", ascending=False))


# Data Visualization - Problem 5: Monthly Sales Visualization
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 14000, 18000, 21000, 19500]

plt.figure(figsize=(7, 5))
plt.plot(months, monthly_sales, marker="o", color="blue", label="Sales")
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(7, 5))
plt.bar(months, monthly_sales, color="orange", label="Sales")
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.legend()
plt.show()


# Data Visualization - Problem 6: Student Marks Visualization
student_names = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
python_marks = [92, 85, 78, 66, 71, 55, 48, 35, 88, 62]

plt.figure(figsize=(8, 5))
plt.bar(student_names, python_marks, color="green")
plt.title("Student Marks in Python")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

excellent = good = average_count = needs_improvement = 0
for m in python_marks:
    if m >= 80:
        excellent += 1
    elif m >= 60:
        good += 1
    elif m >= 40:
        average_count += 1
    else:
        needs_improvement += 1

categories = ["Excellent", "Good", "Average", "Needs Improvement"]
counts = [excellent, good, average_count, needs_improvement]

plt.figure(figsize=(6, 6))
plt.pie(counts, labels=categories, autopct="%1.1f%%", startangle=90)
plt.title("Student Performance Distribution")
plt.show()