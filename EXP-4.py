# Student Record Management with List, Tuple, Dictionary and CSV
import csv
students = [
    {"RollNo": "200", "Name": "Sunitha", "Department": "ECE", "Mark": 89},
    {"RollNo": "108", "Name": "Balaji", "Department": "CSE", "Mark": 97},
    {"RollNo": "106", "Name": "Chinasami", "Department": "AIDS", "Mark": 81}
]
# Tuple example: fixed course details
course = ("Python", 4)
print("Course Tuple:", course)
# Write text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")
# Write CSV file
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)
# Read CSV file
print("\n--- Records from CSV ---")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["RollNo"], row["Name"],
              row["Department"], row["Mark"])