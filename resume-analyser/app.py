from utils import get_text_from_pdf, find_skills, calculate_score

print("Resume Analyzer")

file_path = input("Enter your resume file path: ")

try:
    text = get_text_from_pdf(file_path)

    skills_found = find_skills(text)
    score = calculate_score(skills_found)

    print("\nSkills found:")
    for skill in skills_found:
        print("-", skill)

    print("\nResume Score:", score, "/ 100")

    if score < 50:
        print("You should add more relevant skills.")
    else:
        print("Good resume!")

except Exception as e:
    print("Error reading file:", e)