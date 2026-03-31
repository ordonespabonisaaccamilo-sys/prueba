students = []
id_counter = 1

def generate_id():
    global id_counter
    new_id = id_counter
    id_counter += 1
    return new_id

def find_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

def find_students_by_name(name):
    name_lower = name.lower()
    matches = [s for s in students if name_lower in s["name"].lower()]
    return matches

def print_separator():
    print("-" * 50)

def print_student(student):
    fields = ("id", "name", "age", "program", "status")
    labels = ("ID", "Name", "Age", "Program", "Status")

    print_separator()
    for field, label in zip(fields, labels):
        print(f"  {label:<10}: {student[field]}")
    print_separator()

def register_student():
    print("\n[ Register New Student ]")
    print_separator()

    name = input("  Full name      : ").strip()
    if not name:
        print("  ERROR: Name cannot be empty.")
        return

    while True:
        age_input = input("  Age            : ").strip()
        if age_input.isdigit() and int(age_input) > 0:
            age = int(age_input)
            break
        print("  ERROR: Age must be a positive number. Try again.")

    program = input("  Program/Course : ").strip()
    if not program:
        print("  ERROR: Program cannot be empty.")
        return

    student = {
        "id": generate_id(),
        "name": name,
        "age": age,
        "program": program,
        "status": "active"
    }

    students.append(student)
    print(f"\n  Student '{name}' registered successfully with ID {student['id']}.")

def list_students():
    print("\n[ Student List ]")

    if len(students) == 0:
        print("  No students registered yet.")
        return

    print(f"  Total students: {len(students)}\n")
    for student in students:
        print_student(student)

def search_student():
    print("\n[ Search Student ]")
    print_separator()
    print("  1. Search by ID")
    print("  2. Search by name")
    print_separator()

    option = input("  Choose an option: ").strip()

    if option == "1":
        id_input = input("  Enter student ID: ").strip()

        if not id_input.isdigit():
            print("  ERROR: ID must be a number.")
            return

        student = find_student_by_id(int(id_input))

        if student:
            print("\n  Student found:")
            print_student(student)
        else:
            print(f"  No student found with ID {id_input}.")

    elif option == "2":
        name = input("  Enter name (or part of it): ").strip()

        if not name:
            print("  ERROR: Name cannot be empty.")
            return

        matches = find_students_by_name(name)

        if len(matches) == 0:
            print(f"  No student found with name containing '{name}'.")
        else:
            print(f"\n  {len(matches)} result(s) found:")
            for student in matches:
                print_student(student)
    else:
        print("  ERROR: Invalid option.")

def update_student():
    print("\n[ Update Student ]")

    id_input = input("  Enter the ID of the student to update: ").strip()

    if not id_input.isdigit():
        print("  ERROR: ID must be a number.")
        return

    student = find_student_by_id(int(id_input))

    if not student:
        print(f"  No student found with ID {id_input}.")
        return

    print("\n  Current data:")
    print_student(student)
    print("  Leave a field blank to keep it unchanged.\n")

    new_name = input(f"  New name [{student['name']}]: ").strip()
    if new_name:
        student["name"] = new_name

    new_age = input(f"  New age [{student['age']}]: ").strip()
    if new_age:
        if new_age.isdigit() and int(new_age) > 0:
            student["age"] = int(new_age)
        else:
            print("  WARNING: Invalid age entered — age was not updated.")

    new_program = input(f"  New program [{student['program']}]: ").strip()
    if new_program:
        student["program"] = new_program

    print(f"  Current status: {student['status']}")
    new_status = input("  New status (active/inactive) [leave blank to keep]: ").strip().lower()
    if new_status in ("active", "inactive"):
        student["status"] = new_status
    elif new_status != "":
        print("  WARNING: Invalid status — status was not updated.")

    print(f"\n  Student ID {student['id']} updated successfully.")
 
def delete_student():
    print("\n[ Delete Student ]")
 
    id_input = input("  Enter the ID of the student to delete: ").strip()
 
    if not id_input.isdigit():
        print("  ERROR: ID must be a number.")
        return
 
    student = find_student_by_id(int(id_input))
 
    if not student:
        print(f"  No student found with ID {id_input}.")
        return
 
    print("\n  Student to delete:")
    print_student(student)
 
    confirm = input("  Are you sure you want to delete this student? (yes/no): ").strip().lower()
 
    if confirm == "yes":
        students.remove(student)
        print(f"  Student '{student['name']}' deleted successfully.")
    else:
        print("  Deletion cancelled.")
        
def menu():
    
    while True:
        print(" ----------SISTEMA DE students-----------")
        print("1| ➜ 👤 Add student")
        print("2| ➜ 🔎 See student")
        print("3| ➜ 📃 List")
        print("4| ➜ ♻️ Update information")
        print("0| ➜ 🗑️ Delete student ")
        print("0| ➜ ❌ Go out")
        print("--------------------------------------------")
        op = input("╰┈➤")
        if op == "1":
            register_student()
        elif op == "2":
            list_students()
        elif op == "3":
            search_student()
        elif op == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif op == "0":
            break
        else:
            print("error")
menu()
