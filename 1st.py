print("Welcome to my Python Session - Dhanush")

name = "Dhanush"
year = 4
age = 21
attendance_percent = 96.5

print(name)
print(year)
print(age)
print(attendance_percent)

age = 10

if age < 18:
    print("Not Eligible")

age = 20

if age <= 18:
    print("Not Eligible")
else:
    print("Eligible")

marks = int(input("Enter the mark: "))

if marks >= 90 and marks <= 100:
    print("Grade O")
elif marks >= 80 and marks < 90:
    print("Grade A")
else:
    print("Fail")


def greet(name):
    print("Good Morning", name)
    return 0


greet("Dhanush")

import math

number = 25

print("Square root:", math.sqrt(number))
print("Power:", math.pow(2, 3))

import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers)
print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))

fruits = ["Apple", "Mango", "Banana"]

print(fruits)
print(fruits[0])

fruits.append("Orange")

print(fruits)

student = ("Dhanush", 21, "Python")

print(student)
print(student[0])
print(student[2])

numbers = {10, 20, 30, 20, 10}

print(numbers)

numbers.add(40)

print(numbers)

student = {
    "name": "Dhanush",
    "year": "4th Year",
    "course": "Python"
}

print(student)

print(student["name"])
print(student["course"])

student["year"] = "Final Year"

print(student)


class Student:

    def display(self):
        print("I am a student")
        print("I am learning Python")


student1 = Student()
student1.display()


class Student:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def display(self):
        print("Name:", self.name)
        print("Year:", self.year)


student1 = Student("Dhanush", 4)
student1.display()


class Animal:

    def eat(self):
        print("Animal eats")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


dog1 = Dog()
dog1.eat()
dog1.bark()


class Student:

    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark

    def display(self):
        print("Name:", self.name)
        print("Mark:", self.__mark)


student = Student("Dhanush", 85)
student.display()


class Dog:

    def sound(self):
        print("Dog says Woof")


class Cat:

    def sound(self):
        print("Cat says Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")


car = Car()
car.start()