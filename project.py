students = []
marks = []
numbers = int(input("Enter the number of students: "))


for i in range (numbers):
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

while True:
    print("===== Student Marks Manager =====")
    print("1. Display Students")
    print("2. Average Marks")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

   
    if choice == '1':
        display_students()

    elif choice == '2':
        average_marks()

    elif choice == '3':
        highest_marks()

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.\n")









