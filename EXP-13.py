import pandas as pd
import re
from google.colab import files

uploaded = files.upload()
df = pd.read_csv("experiment_13_study_materials.csv")

def tokenize(text):
    return set(re.findall(r"[a-zA-Z]+", str(text).lower()))

def retrieve_material(query):
    query_words = tokenize(query)
    scores = []
    for _, row in df.iterrows():
        searchable_text = " ".join([
            row["Topic"], row["Concept"], row["Explanation"], row["Keywords"]
        ])
        material_words = tokenize(searchable_text)
        score = len(query_words & material_words) / max(len(query_words), 1)
        scores.append(score)
    best_index = scores.index(max(scores))
    if scores[best_index] == 0:
        return None, 0
    return df.iloc[best_index], scores[best_index]

def study_assistant(query):
    material, score = retrieve_material(query)
    if material is None:
        print("No matching material found. Try another concept.")
        return
    print("\n----- PERSONALIZED STUDY NOTES -----")
    print("Topic       :", material["Topic"])
    print("Concept     :", material["Concept"])
    print("Explanation :", material["Explanation"])
    print("Match score :", round(score * 100, 2), "%")
    print("\n----- QUICK QUIZ -----")
    print("Question    :", material["Quiz_Question"])
    print("Difficulty  :", material["Difficulty"])
    print("Answer      :", material["Answer"])

print("Available concepts:", ", ".join(df["Concept"].tolist()))
query = input("\nEnter a topic or concept to study: ")
study_assistant(query)
print("\nStudy assistant session completed.")
print("Note: Matching is based on CSV keyword overlap, not a live Generative AI model.")
