from PyPDF2 import PdfReader

def get_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content.lower()

    return text


def find_skills(text):
    skills_list = [
        "python", "java", "c++", "sql",
        "machine learning", "data analysis",
        "html", "css", "javascript"
    ]

    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found


def calculate_score(skills):
    score = len(skills) * 10

    if score > 100:
        score = 100

    return score