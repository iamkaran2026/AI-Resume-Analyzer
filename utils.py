import spacy
nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    skills = ["python", "machine learning", "data analysis", "sql", "nlp", "tensorflow", "pandas"]  # example
    text = text.lower()
    return [skill for skill in skills if skill in text]

def clean_text(text):
    return " ".join(text.split()).strip().lower()
