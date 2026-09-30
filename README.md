Python Student Management System

A console-based Student Management System developed using Python. The project allows users to add, view, search, update, delete, analyze, and manage student records with JSON and CSV file handling.

Features
Add new student records
View all students in a formatted table
Search student by ID
Search students by name
Search students by branch
Search students by marks range
Search students by age
Update student details
Delete individual students
Calculate average marks
Find the top-performing student
Sort students by marks
Count total students
Count PASS and FAIL students
Filter students by PASS/FAIL
Filter students by grade
Generate branch-wise statistics
Generate performance summary
Find highest and lowest marks
Generate overall student statistics
Generate individual student reports
Export student data to CSV
Import student data from CSV
Store student data permanently using JSON
Delete all student records with confirmation
Input validation and error handling
Technologies Used
Python
JSON
CSV
File Handling
Functions
Lists and Dictionaries
Loops
Conditional Statements
Exception Handling
Modular Programming
Project Structure
python-student-management-system/
│
├── main.py
├── student_operations.py
├── file_handler.py
├── students.json
├── students.csv
└── README.md
main.py

Controls the application menu and connects all project modules.

student_operations.py

Contains the main student operations such as adding, searching, updating, deleting, sorting, filtering, and calculating statistics.

file_handler.py

Handles saving and loading student data using JSON and importing/exporting data using CSV.

students.json

Stores student records permanently.

students.csv

Stores student information in CSV format for easy viewing and data exchange.

Grading System
Marks	Grade	Result
90–100	A	PASS
75–89	B	PASS
60–74	C	PASS
40–59	D	PASS
Below 40	F	FAIL
Performance Levels
Marks	Performance
90–100	Excellent
75–89	Good
60–74	Average
40–59	Needs Improvement
Below 40	Poor
How to Run
Step 1: Install Python

Install Python on your computer and make sure Python is added to PATH.

Step 2: Open the Project

Open the project folder in VS Code.

Step 3: Open Terminal

In VS Code, select:

Terminal → New Terminal
Step 4: Run the Application
python main.py
Sample Operations
1. Add Student
2. View Students
3. Search Student by ID
4. Search by Name
5. Search by Branch
6. Search by Marks
7. Search by Age
8. Update Student
9. Delete Student
10. Calculate Average Marks
...
25. Exit
Data Storage

The application uses:

JSON for permanent storage of student records.
CSV for exporting and importing student information.
Future Enhancements
Add a graphical user interface using Tkinter
Add a database using MySQL or SQLite
Add user login and authentication
Generate PDF student reports
Add attendance management
Add subject-wise marks
Add charts and data visualization
Deploy the application as a web application
Author

Priya

B.Tech – Electronics and Communication Engineering

License

This project is created for learning, practice, and portfolio purposes.