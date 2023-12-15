#Exercise: Student Grade System
#Create a program that manages a student grade system using Python lists and their methods. The program should allow the user to perform the following actions:

# Add Student Grades: Allow the user to add student names and their respective grades to a list.
# Remove Student: Allow the user to remove a student and their grade from the list by providing the student's name.
# Display Student Grades: Display the list of student names and their corresponding grades.
# Calculate Average Grade: Calculate and display the average grade of all students.
# Sort Students by Grade: Sort and display the students based on their grades in ascending order.
# Exit the Program


while True:
    print("Welcome to Student Grade System!\n1. Add Student Grades\n2. Remove Student\n3. Display Student Grades\n4. Calculate Average Grade\n5. Sort Students by Grade\n6. Exit")
    student_grade = []
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            student_grade.append({"name": name, "grade": grade})
            print("Student grades added successfully!")

        elif choice == 2:
            name_to_remove = input("Enter name of the Student to remove: ")
            removed = False
            for student in student_grade:
                if student["name"] == name_to_remove:
                    student_grade.remove(student)
                    removed = True
                    print(f"{name_to_remove} has been removed from the list.")
                    break

            if not removed:
                print(f"No student with the name '{name_to_remove}' found.")

        elif choice == 3:
            if len(student_grade) > 0:
                for record in student_grade:
                    print(record)
            else:
                print("No records found")

        elif choice == 4:
            if len(student_grade) < 1:
                print("No records found")
            else:
                all_grades = [record['grade'] for record in student_grade]
                average_grade = sum(all_grades) / len(all_grades)
                print("Average grade:", average_grade)

        elif choice == 5:
            student_grade.sort(key=lambda x: x['grade'])
            for record in student_grade:
                print(f"Name: {record['name']}, Grade: {record['grade']}")

        elif choice == 6:
            break
    except Exception as e:
        print("Not a valid input, Please try again")