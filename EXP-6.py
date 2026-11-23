# Pandas Series and DataFrame
import pandas as pd

marks = pd.Series([82, 94, 76, 89, 91],
                  index=["A", "B", "C", "D", "E"])
print("--- Pandas Series ---")
print(marks)

data = {
    "RollNo": [201, 202, 203, 204, 205],
    "Name": ["Karthik", "Divya", "Harish", "Kavya", "Manoj"],
    "Department": ["AI&DS", "CSE", "IT", "AI&DS", "ECE"],
    "Mark": [82, 94, 76, 89, 91]
}
df = pd.DataFrame(data)
print("\n--- DataFrame ---")
print(df)

print("\nAverage Mark:", round(df["Mark"].mean(), 2))
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])
