def calculate_result(marks):

    if marks >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    return result, grade


def performance_level(marks):

    if marks >= 90:
        return "Excellent"
    elif marks >= 75:
        return "Good"
    elif marks >= 60:
        return "Average"
    elif marks >= 40:
        return "Needs Improvement"
    else:
        return "Poor"


def id_exists(students, student_id):

    for student in students:

        if student["id"] == student_id:
            return True

    return False


def add_student(students):

    student_id = input("Enter Student ID: ")

    if id_exists(students, student_id):
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid age.")

    branch = input("Enter Branch: ")

    while True:
        try:
            marks = float(input("Enter Marks: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully.")


def display_student(student):

    result, grade = calculate_result(student["marks"])
    performance = performance_level(student["marks"])

    print("ID          :", student["id"])
    print("Name        :", student["name"])
    print("Age         :", student["age"])
    print("Branch      :", student["branch"])
    print("Marks       :", student["marks"])
    print("Result      :", result)
    print("Grade       :", grade)
    print("Performance :", performance)
    print("--------------------------------")


def display_students_table(students):

    if len(students) == 0:
        print("No students found.")
        return

    print()
    print("=" * 90)

    print(
        f"{'ID':<8}"
        f"{'Name':<18}"
        f"{'Age':<6}"
        f"{'Branch':<10}"
        f"{'Marks':<8}"
        f"{'Result':<10}"
        f"{'Grade':<8}"
        f"{'Performance':<18}"
    )

    print("-" * 90)

    for student in students:

        result, grade = calculate_result(student["marks"])
        performance = performance_level(student["marks"])

        print(
            f"{student['id']:<8}"
            f"{student['name']:<18}"
            f"{student['age']:<6}"
            f"{student['branch']:<10}"
            f"{student['marks']:<8}"
            f"{result:<10}"
            f"{grade:<8}"
            f"{performance:<18}"
        )

    print("=" * 90)


def view_students(students):

    if len(students) == 0:
        print("No students available.")
        return

    print()
    print("                 STUDENT LIST")

    display_students_table(students)


def search_student(students):

    if len(students) == 0:
        print("No students available.")
        return

    student_id = input("Enter Student ID to search: ")

    for student in students:

        if student["id"] == student_id:

            print()
            print("Student Found")
            print("--------------------------------")

            display_student(student)

            return

    print("Student not found.")


def search_by_name(students):

    search_name = input("Enter student name: ")

    matching_students = []

    for student in students:

        if search_name.lower() in student["name"].lower():

            matching_students.append(student)

    display_students_table(matching_students)


def search_by_branch(students):

    search_branch = input("Enter branch to search: ")

    matching_students = []

    for student in students:

        if student["branch"].lower() == search_branch.lower():

            matching_students.append(student)

    display_students_table(matching_students)


def search_by_marks(students):

    try:
        minimum = float(input("Enter minimum marks: "))
        maximum = float(input("Enter maximum marks: "))

        if minimum < 0 or maximum > 100 or minimum > maximum:
            print("Invalid marks range.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    matching_students = []

    for student in students:

        if minimum <= student["marks"] <= maximum:

            matching_students.append(student)

    display_students_table(matching_students)


def search_by_age(students):

    try:
        search_age = int(input("Enter age to search: "))

    except ValueError:
        print("Please enter a valid age.")
        return

    matching_students = []

    for student in students:

        if student["age"] == search_age:

            matching_students.append(student)

    display_students_table(matching_students)


def update_student(students):

    if len(students) == 0:
        print("No students available.")
        return

    student_id = input("Enter Student ID to update: ")

    for student in students:

        if student["id"] == student_id:

            print("Student found.")

            name = input("Enter new name: ")

            while True:
                try:
                    age = int(input("Enter new age: "))

                    if age <= 0:
                        print("Age must be greater than 0.")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid age.")

            branch = input("Enter new branch: ")

            while True:
                try:
                    marks = float(input("Enter new marks: "))

                    if marks < 0 or marks > 100:
                        print("Marks must be between 0 and 100.")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid number.")

            student["name"] = name
            student["age"] = age
            student["branch"] = branch
            student["marks"] = marks

            print("Student updated successfully.")

            return

    print("Student not found.")


def delete_student(students):

    if len(students) == 0:
        print("No students available.")
        return

    student_id = input("Enter Student ID to delete: ")

    for student in students:

        if student["id"] == student_id:

            print()
            print("Student Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Marks:", student["marks"])

            confirmation = input(
                "Are you sure you want to delete this student? (yes/no): "
            ).lower()

            if confirmation == "yes":

                students.remove(student)

                print("Student deleted successfully.")

            else:

                print("Delete operation cancelled.")

            return

    print("Student not found.")


def calculate_average(students):

    if len(students) == 0:
        print("No students available.")
        return

    total_marks = 0

    for student in students:
        total_marks = total_marks + student["marks"]

    average = total_marks / len(students)

    print("Average Marks:", round(average, 2))


def find_top_student(students):

    if len(students) == 0:
        print("No students available.")
        return

    top_student = students[0]

    for student in students:

        if student["marks"] > top_student["marks"]:
            top_student = student

    print()
    print("========== TOP STUDENT ==========")

    display_student(top_student)


def sort_students(students):

    if len(students) == 0:
        print("No students available.")
        return

    students.sort(
        key=lambda student: student["marks"],
        reverse=True
    )

    print("Students sorted by marks.")


def count_students(students):

    print("Total Students:", len(students))


def count_pass_fail(students):

    if len(students) == 0:
        print("No students available.")
        return

    pass_count = 0
    fail_count = 0

    for student in students:

        if student["marks"] >= 40:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    print("Passed Students:", pass_count)
    print("Failed Students:", fail_count)


def filter_pass_fail(students):

    if len(students) == 0:
        print("No students available.")
        return

    choice = input("Enter PASS or FAIL: ").upper()

    if choice != "PASS" and choice != "FAIL":
        print("Please enter only PASS or FAIL.")
        return

    matching_students = []

    for student in students:

        if choice == "PASS" and student["marks"] >= 40:
            matching_students.append(student)

        elif choice == "FAIL" and student["marks"] < 40:
            matching_students.append(student)

    display_students_table(matching_students)


def filter_by_grade(students):

    if len(students) == 0:
        print("No students available.")
        return

    search_grade = input(
        "Enter grade (A/B/C/D/F): "
    ).upper()

    if search_grade not in ["A", "B", "C", "D", "F"]:
        print("Invalid grade.")
        return

    matching_students = []

    for student in students:

        result, grade = calculate_result(student["marks"])

        if grade == search_grade:
            matching_students.append(student)

    display_students_table(matching_students)


def branch_statistics(students):

    if len(students) == 0:
        print("No students available.")
        return

    branches = []

    for student in students:

        branch = student["branch"].upper()

        if branch not in branches:
            branches.append(branch)

    print()
    print("========== BRANCH STATISTICS ==========")

    for branch in branches:

        count = 0
        total_marks = 0

        for student in students:

            if student["branch"].upper() == branch:

                count = count + 1
                total_marks = total_marks + student["marks"]

        average = total_marks / count

        print()
        print("Branch   :", branch)
        print("Students :", count)
        print("Average  :", round(average, 2))

    print("=======================================")


def performance_summary(students):

    if len(students) == 0:
        print("No students available.")
        return

    excellent = 0
    good = 0
    average = 0
    needs_improvement = 0
    poor = 0

    for student in students:

        performance = performance_level(student["marks"])

        if performance == "Excellent":
            excellent = excellent + 1

        elif performance == "Good":
            good = good + 1

        elif performance == "Average":
            average = average + 1

        elif performance == "Needs Improvement":
            needs_improvement = needs_improvement + 1

        elif performance == "Poor":
            poor = poor + 1

    print()
    print("========== PERFORMANCE SUMMARY ==========")
    print("Excellent           :", excellent)
    print("Good                :", good)
    print("Average             :", average)
    print("Needs Improvement   :", needs_improvement)
    print("Poor                :", poor)
    print("=========================================")


def highest_lowest_student(students):

    if len(students) == 0:
        print("No students available.")
        return

    highest = students[0]
    lowest = students[0]

    for student in students:

        if student["marks"] > highest["marks"]:
            highest = student

        if student["marks"] < lowest["marks"]:
            lowest = student

    print()
    print("========== HIGHEST MARKS ==========")

    display_student(highest)

    print()
    print("========== LOWEST MARKS ==========")

    display_student(lowest)


def student_statistics(students):

    if len(students) == 0:
        print("No students available.")
        return

    total_students = len(students)

    total_marks = 0

    highest_marks = students[0]["marks"]
    lowest_marks = students[0]["marks"]

    pass_count = 0
    fail_count = 0

    for student in students:

        marks = student["marks"]

        total_marks = total_marks + marks

        if marks > highest_marks:
            highest_marks = marks

        if marks < lowest_marks:
            lowest_marks = marks

        if marks >= 40:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    average_marks = total_marks / total_students

    print()
    print("========== STUDENT STATISTICS ==========")
    print("Total Students :", total_students)
    print("Average Marks  :", round(average_marks, 2))
    print("Highest Marks  :", highest_marks)
    print("Lowest Marks   :", lowest_marks)
    print("Passed Students:", pass_count)
    print("Failed Students:", fail_count)
    print("========================================")


def student_report(students):

    if len(students) == 0:
        print("No students available.")
        return

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            print()
            print("========== STUDENT REPORT ==========")

            display_student(student)

            print("====================================")

            return

    print("Student not found.")


def delete_all_students(students):

    if len(students) == 0:
        print("No students available.")
        return

    print()
    print("WARNING: This will delete ALL students.")

    confirmation = input(
        "Type YES to confirm deletion: "
    ).upper()

    if confirmation == "YES":

        students.clear()

        print("All students deleted successfully.")

    else:

        print("Delete all operation cancelled.")