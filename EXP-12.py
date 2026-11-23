import pandas as pd
from google.colab import files
from pathlib import Path

uploaded = files.upload()
df = pd.read_csv("experiment_12_technical_generation.csv")

templates = {
    "Palindrome Checker": '''import string
def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
''',
    "Prime Number Check": '''import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
''',
    "Fibonacci Series": '''def fibonacci_series(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq
''',
    "Dictionary Merge": '''def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged
''',
    "File Line Counter": '''def count_non_empty_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())
'''
}

output_dir = Path("generated_technical_content")
output_dir.mkdir(exist_ok=True)

print("----- TECHNICAL CONTENT AND PYTHON PROGRAM GENERATION -----")
for _, row in df.iterrows():
    topic = row["Topic"]
    code = templates[topic]
    explanation = (
        f"Topic: {topic}\nAudience: {row['Audience']}\n"
        f"Task: {row['Task_Description']}\n"
        f"Requirements: {row['Requirements']}\n"
        "Approach: validate inputs, process data and present a clear result."
    )
    file_stem = row["Task_ID"].lower()
    (output_dir / f"{file_stem}.py").write_text(code, encoding="utf-8")
    (output_dir / f"{file_stem}_notes.txt").write_text(explanation, encoding="utf-8")
    print(f"\nTask ID: {row['Task_ID']} | Topic: {topic}")
    print(explanation)
    print("Saved:", f"{file_stem}.py", "and", f"{file_stem}_notes.txt")

print("\nTotal generated files:", len(list(output_dir.iterdir())))
print("Template-based generation completed. No external LLM is called.")
