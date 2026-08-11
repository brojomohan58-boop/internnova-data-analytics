”””InternNova Data Analytics Internship
Week 1 Assignment: Python Fundamentals for Data Analytics
Submitted by: Brojo Mohan Dutta
Duration: 1 Week (7 Days)”””   
 
# Task 1: Python Basics
print("Welcome to Python Fundamentals for Data Analytics!")
 
name = input("Enter your Name: ")
college = input("Enter your College Name: ")
branch = input("Enter your Branch: ")
 
print("\n----- Student Details -----")
print(f"Name    : {name}")
print(f"College : {college}")
print(f"Branch  : {branch}")


# Task 2: Variables & Data Types
age = 24                       # Integer
cgpa = 7.02                    # Float
student_name = "Brojo"         # String
is_placed = False              # Boolean
 
print("Variable:", age, "-> Type:", type(age))
print("Variable:", cgpa, "-> Type:", type(cgpa))
print("Variable:", student_name, "-> Type:", type(student_name))
print("Variable:", is_placed, "-> Type:", type(is_placed))

 
# Task 3: Operators - Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
 
print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division       :", num1 / num2 if num2 != 0 else "Undefined (division by zero)")
print("Modulus        :", num1 % num2 if num2 != 0 else "Undefined (division by zero)")


# Task 4: Conditional Statements - Grade Calculator
marks = float(input("Enter your marks: "))
 
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"
 
print(f"Grade: {grade}")


# Task 5: Loops
# 1. Print numbers from 1 to 20 using a for loop
print("Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print()
 
# 2. Multiplication table of a number
num = int(input("\nEnter a number for multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
 
# 3. Print even numbers from 1 to 50 using a while loop
print("\nEven numbers from 1 to 50:")
n = 1
while n <= 50:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1
print()

 
# Task 6: Functions
def square(n):
    """Returns the square of a number"""
    return n * n
 
def average(a, b, c):
    """Returns the average of three numbers"""
    return (a + b + c) / 3
 
num = float(input("Enter a number to find its square: "))
print(f"Square of {num} = {square(num)}")
 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print(f"Average of {a}, {b}, {c} = {average(a, b, c)}")


# Task 7: Strings & Collections 
# --- String Operations ---
text = "Data Analytics"
print("Original String:", text)
print("Upper Case:", text.upper())
print("Lower Case:", text.lower())
print("Replace 'Data' with 'Big Data':", text.replace("Data", "Big Data"))
print("Index of 'Analytics':", text.find("Analytics"))
 
# --- List Operations ---
tools = ["Excel", "SQL", "Python"]
tools.append("Tableau")
print("\nTools after add:", tools)
tools.remove("Excel")
print("Tools after remove:", tools)
tools.sort()
print("Sorted list:", tools)
 
# --- Tuple Creation and Indexing ---
coordinates = (10, 20, 30)
print("\nTuple:", coordinates)
print("First element:", coordinates[0])
print("Last element:", coordinates[-1])
 
# --- Dictionary storing student information ---
student = {
    "name": "Brojo Mohan Dutta",
    "branch": "B.Sc(Mathematics)",
    "cgpa": 7.02
}
print("\nStudent Name:", student["name"])
print("Student Dictionary:", student)
 
# --- Set Operations ---
skills = {"Python", "SQL", "Excel"}
skills.add("Power BI")
print("\nSkills after add:", skills)
skills.remove("Excel")
print("Skills after remove:", skills)

# Task 8: Basic File Handling
 
# Create and write to a text file
with open("introduction.txt", "w") as file:
    file.write("Hi, my name is Brojo.\n")
    file.write("I am pursuing a career as a Data Analyst.\n")
    file.write("I am currently doing my Data Analytics Internship at InternNova.\n")
 
# Read and display the file contents
with open("introduction.txt", "r") as file:
    content = file.read()
    print("----- File Contents -----")
    print(content)


# Task 9: Mini Python Project - Student Record Management System
students = []
 
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    branch = input("Enter branch: ")
    students.append({"name": name, "age": age, "branch": branch})
    print(f"Student '{name}' added successfully.\n")
 
def display_students():
    if not students:
        print("No student records found.\n")
        return
    print("----- Student Records -----")
    for s in students:
        print(f"Name: {s['name']} | Age: {s['age']} | Branch: {s['branch']}")
    print()
 
def search_student():
    name = input("Enter name to search: ")
    found = [s for s in students if s["name"].lower() == name.lower()]
    if found:
        for s in found:
            print(f"Found -> Name: {s['name']}, Age: {s['age']}, Branch: {s['branch']}\n")
    else:
        print("Student not found.\n")
 
def delete_student():
    name = input("Enter name to delete: ")
    global students
    before = len(students)
    students = [s for s in students if s["name"].lower() != name.lower()]
    if len(students) < before:
        print(f"Student '{name}' deleted successfully.\n")
    else:
        print("Student not found.\n")
 
def menu():
    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
 
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
 
if __name__ == "__main__":
    menu()


