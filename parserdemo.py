import pdfminer.high_level
import spacy

def extract_text_from_pdf(pdf_path):
    return pdfminer.high_level.extract_text(pdf_path)

def parse_resume(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    return {"extracted_text": text}

pdf_path = 'Akershak Python Resume.pdf'
text = extract_text_from_pdf(pdf_path)
data = parse_resume(text)
print(data)
# print("Name:", data["name"])
# print("Email:", data["email"])
# print("Mobile Number:", data["mobile_number"])
# print("Skills:", data["skills"])
# print("College Name:", data["college_name"])
# print("Degree:", data["degree"])
# print("Designation:", data["designation"])
# print("Company Names:", data["company_names"])
# print("No Of Pages:", data["no_of_pages"])
# print("Total Experience:", data["total_experience"])