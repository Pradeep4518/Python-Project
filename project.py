students = []
marks = []

def add_student():
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))
    students.append(name)
    marks.append(mark)
    print("Student added successfully!\n")

def display_students():
    if len(students) == 0:
        print("No records found.\n")
    else:
        print("\nStudent Records:")
        for i in range(len(students)):
            print(students[i], ":", marks[i])
        print()

def average_marks():
    if len(marks) == 0:
        print("No data to calculate average.\n")
    else:
        avg = sum(marks) / len(marks)
        print("Average Marks:", avg, "\n")

def highest_marks():
    if len(marks) == 0:
        print("No data to find topper.\n")
    else:
        max_mark = max(marks)
        index = marks.index(max_mark)
        print("Topper:", students[index], "-", max_mark, "\n")

numbers = int(input("Enter the number of students: "))
count = 0 

while True:
    print("===== Student Marks Manager =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Average Marks")
    print("4. Find Topper")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        for i in range (numbers):
            if count < numbers:
                add_student()
                count += 1
            else:
                print("You already added all students!\n")

    elif choice == '2':
        display_students()

    elif choice == '3':
        average_marks()

    elif choice == '4':
        highest_marks()

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.\n")
