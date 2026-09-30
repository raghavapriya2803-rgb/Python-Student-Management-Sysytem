from student_operations import (
    add_student,
    view_students,
    search_student,
    search_by_name,
    search_by_branch,
    search_by_marks,
    search_by_age,
    update_student,
    delete_student,
    calculate_average,
    find_top_student,
    sort_students,
    count_students,
    count_pass_fail,
    filter_pass_fail,
    filter_by_grade,
    branch_statistics,
    performance_summary,
    highest_lowest_student,
    student_statistics,
    student_report,
    delete_all_students
)

from file_handler import (
    load_students,
    save_students,
    export_to_csv,
    import_from_csv
)


def show_menu():

    print()
    print("=" * 50)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1.  Add Student")
    print("2.  View Students")
    print("3.  Search Student by ID")
    print("4.  Search by Name")
    print("5.  Search by Branch")
    print("6.  Search by Marks")
    print("7.  Search by Age")
    print("8.  Update Student")
    print("9.  Delete Student")
    print("10. Calculate Average Marks")
    print("11. Find Top Student")
    print("12. Sort Students")
    print("13. Count Students")
    print("14. Count Pass/Fail")
    print("15. Filter PASS/FAIL Students")
    print("16. Filter by Grade")
    print("17. Branch Statistics")
    print("18. Performance Summary")
    print("19. Highest & Lowest Student")
    print("20. Student Statistics")
    print("21. Student Report")
    print("22. Export to CSV")
    print("23. Import from CSV")
    print("24. Delete All Students")
    print("25. Exit")

    print("=" * 50)


students = load_students()


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student(students)
        save_students(students)

    elif choice == "2":

        view_students(students)

    elif choice == "3":

        search_student(students)

    elif choice == "4":

        search_by_name(students)

    elif choice == "5":

        search_by_branch(students)

    elif choice == "6":

        search_by_marks(students)

    elif choice == "7":

        search_by_age(students)

    elif choice == "8":

        update_student(students)
        save_students(students)

    elif choice == "9":

        delete_student(students)
        save_students(students)

    elif choice == "10":

        calculate_average(students)

    elif choice == "11":

        find_top_student(students)

    elif choice == "12":

        sort_students(students)
        save_students(students)

    elif choice == "13":

        count_students(students)

    elif choice == "14":

        count_pass_fail(students)

    elif choice == "15":

        filter_pass_fail(students)

    elif choice == "16":

        filter_by_grade(students)

    elif choice == "17":

        branch_statistics(students)

    elif choice == "18":

        performance_summary(students)

    elif choice == "19":

        highest_lowest_student(students)

    elif choice == "20":

        student_statistics(students)

    elif choice == "21":

        student_report(students)

    elif choice == "22":

        export_to_csv(students)

    elif choice == "23":

        import_from_csv(students)

    elif choice == "24":

        delete_all_students(students)
        save_students(students)

    elif choice == "25":

        print()
        print("Thank you for using Student Management System!")
        print("Program closed.")
        break

    else:

        print()
        print("Invalid choice.")
        print("Please enter a number from 1 to 25.")
   


