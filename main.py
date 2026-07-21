# Student Marks Manager using Functions

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records")
        for name, marks in students.items():
            print(name, ":", marks)

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print("Marks of", name, "=", students[name])
    else:
        print("Student not found.")

def update_marks():
    name = input("Enter student name: ")
    if name in students:
        marks = float(input("Enter new marks: "))
        students[name] = marks
        print("Marks updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter student name: ")
    if name in students:
        del students[name]
        print("Student record deleted.")
    else:
        print("Student not found.")

while True:
    print("\n===== Student Marks Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
