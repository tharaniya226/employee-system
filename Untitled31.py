#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tkinter mysql-connector-python pandas


# In[ ]:


import json

# Load employee data from a file (if exists)
try:
    with open("employees.json", "r") as file:
        employees = json.load(file)
except FileNotFoundError:
    employees = {}

# Function to save data to file
def save_data():
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)

# Function to add a new employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print("Employee ID already exists!\n")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")
    
    employees[emp_id] = {"name": name, "age": age, "department": department, "salary": salary}
    save_data()
    print("Employee Added Successfully!\n")

# Function to view all employees
def view_employees():
    if not employees:
        print("No Employees Found.\n")
        return
    print("\nID | Name | Age | Department | Salary")
    print("-" * 40)
    for emp_id, details in employees.items():
        print(f"{emp_id} | {details['name']} | {details['age']} | {details['department']} | {details['salary']}")
    print()

# Function to search for an employee
def search_employee():
    emp_id = input("Enter Employee ID to Search: ")
    if emp_id in employees:
        emp = employees[emp_id]
        print(f"\nID: {emp_id}\nName: {emp['name']}\nAge: {emp['age']}\nDepartment: {emp['department']}\nSalary: {emp['salary']}\n")
    else:
        print("Employee Not Found.\n")

# Function to update employee details
def update_employee():
    emp_id = input("Enter Employee ID to Update: ")
    if emp_id in employees:
        salary = input("Enter New Salary: ")
        employees[emp_id]["salary"] = salary
        save_data()
        print("Employee Salary Updated Successfully!\n")
    else:
        print("Employee Not Found.\n")

# Function to delete an employee
def delete_employee():
    emp_id = input("Enter Employee ID to Delete: ")
    if emp_id in employees:
        del employees[emp_id]
        save_data()
        print("Employee Deleted Successfully!\n")
    else:
        print("Employee Not Found.\n")

# Main menu
while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee by ID")
    print("4. Update Employee Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        update_employee()
    elif choice == '5':
        delete_employee()
    elif choice == '6':
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid Choice! Try Again.\n")


# In[ ]:




