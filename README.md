Student Management System
A console-based student management system built with Python.
Developed as the Module 1 Python Performance Test.

How to Run
Make sure you have Python 3 installed. Then run:
bashpython student_management.py
No external libraries needed — uses only built-in Python.

Features

Register a new student with ID, name, age, program and status
List all registered students
Search a student by ID or by name (partial match supported)
Update any field of an existing student
Delete a student with confirmation prompt
Input validation on every field — the program never crashes on bad input
Auto-generated IDs — each student gets a unique ID automatically


Data Structure
Each student is stored as a dictionary inside a list:
python{
    "id":      1,
    "name":    "Ana García",
    "age":     20,
    "program": "Software Development",
    "status":  "active"
}
A tuple is used to define the fixed display order of fields when printing.

Usage Examples
Register a student
Select an option: 1

[ Register New Student ]
  Full name      : Ana García
  Age            : 20
  Program/Course : Software Development

  Student 'Ana García' registered successfully with ID 1.
Search by name
Select an option: 3

[ Search Student ]
  1. Search by ID
  2. Search by name
  Choose an option: 2
  Enter name (or part of it): ana

  1 result(s) found:
  --------------------------------------------------
  ID        : 1
  Name      : Ana García
  Age       : 20
  Program   : Software Development
  Status    : active
  --------------------------------------------------
Update a student
Select an option: 4
  Enter the ID of the student to update: 1
  New name [Ana García]:
  New age [20]: 21
  New program [Software Development]:
  New status (active/inactive) [leave blank to keep]:

  Student ID 1 updated successfully
