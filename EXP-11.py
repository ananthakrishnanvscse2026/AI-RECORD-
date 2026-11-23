import pandas as pd
from google.colab import files

uploaded = files.upload()
df = pd.read_csv("experiment_11_prompting_techniques.csv")

positive_words = {"clean", "fast", "amazing", "sturdy", "neat", "secure", "great"}
negative_words = {"damaged", "missing", "overheats", "poor", "broken", "unavailable"}

def sentiment_demo(sentence):
    words = set(sentence.lower().replace(".", "").replace(",", "").split())
    score = len(words & positive_words) - len(words & negative_words)
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"

def construct_prompt(row):
    role = row["Role"]
    task = row["Task"]
    text = row["Input_Text"]
    technique = row["Technique"]
    
    if technique.lower() == "zero-shot":
        return f"You are a {role}. {task}: {text}"
    if technique.lower() == "one-shot":
        return (f"You are a {role}. {task}. Example: "
                f"{row['Example_Input']} -> {row['Example_Output']}. New input: {text}")
    if technique.lower() == "few-shot":
        return (f"You are a {role}. {task}. Examples: "
                f"{row['Example_Input']}. New input: {text}")
    return f"Act as {role}. {task}: {text}"

print("----- ROLE-BASED AND EXAMPLE-BASED PROMPTING -----")
for _, row in df.iterrows():
    prompt = construct_prompt(row)
    if "sentiment" in row["Task"].lower():
        response = sentiment_demo(row["Input_Text"])
    elif "priority" in row["Task"].lower():
        response = "High" if "down" in row["Input_Text"].lower() else "Low"
    else:
        response = "Suggested rewrite: I will be unable to attend today's meeting."
        
    print(f"\nID: {row['Example_ID']} | Technique: {row['Technique']}")
    print("Constructed prompt:", prompt)
    print("Python demonstration response:", response)

print("\nDemonstration completed. Responses use predefined Python rules, not a live LLM.")
