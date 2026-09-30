import json
import csv

from student_operations import calculate_result, id_exists

def save_students(students):

    with open("students.json", "w") as file:

        json.dump(students, file, indent=4)

    print("Student data saved successfully.")


def load_students():

    try:

        with open("students.json", "r") as file:

            students = json.load(file)

            if not isinstance(students, list):

                print("Invalid data in students.json.")

                return []

            return students

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        print("students.json is empty or corrupted.")
        print("Starting with an empty student list.")

        return []


def export_to_csv(students):

    if len(students) == 0:

        print("No students available to export.")

        return

    with open("students.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student ID",
            "Name",
            "Age",
            "Branch",
            "Marks",
            "Result",
            "Grade"
        ])

        for student in students:

            result, grade = calculate_result(student["marks"])

            writer.writerow([
                student["id"],
                student["name"],
                student["age"],
                student["branch"],
                student["marks"],
                result,
                grade
            ])

    print("Student data exported successfully to students.csv")


def import_from_csv(students):

    try:

        with open("students.csv", "r", newline="") as file:

            reader = csv.DictReader(file)

            imported_count = 0

            for row in reader:

                student_id = row["Student ID"]

                if id_exists(students, student_id):

                    print(
                        "Student ID",
                        student_id,
                        "already exists. Skipping."
                    )

                    continue

                student = {
                    "id": student_id,
                    "name": row["Name"],
                    "age": int(row["Age"]),
                    "branch": row["Branch"],
                    "marks": float(row["Marks"])
                }

                students.append(student)

                imported_count = imported_count + 1

        save_students(students)

        print(
            imported_count,
            "students imported successfully."
        )

    except FileNotFoundError:

        print("students.csv file not found.")

    except ValueError:

        print("Invalid data found in CSV file.")