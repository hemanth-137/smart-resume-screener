import re
from skills_list import skills_list
import PyPDF2

resume_path = r"C:\Users\heman\Desktop\hemanth_resume_sep_25.pdf"

def extract_text_from_pdf(pdf_path: str) -> str | None:

    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)      
            full_text = ""
            for page in reader.pages:
                full_text += page.extract_text() or ""
                
            return full_text            
    except FileNotFoundError:
        print(f"Error: The file was not found at {pdf_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return None


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s,.@-]', '', text)
    return text.strip()

def extract_info(resume_text):
    data = {}
    data['email'] = re.findall(r'[\w\.-]+@[\w\.-]+', resume_text)
    data['phone'] = re.findall(r'\+?\d[\d -]{8,12}\d', resume_text)
    data['skills'] = [skill for skill in skills_list if skill.lower() in resume_text.lower()]
    
    edu_keywords = ['btech','mtech','b.e','bachelor','master','degree','university','college']
    data['education'] = [line for line in resume_text.split('.') if any(k in line.lower() for k in edu_keywords)]
    
    exp_keywords = ['intern','experience','worked','developer','engineer']
    data['experience'] = [line for line in resume_text.split('.') if any(k in line.lower() for k in exp_keywords)]
    
    return data

def data_flow(path):
    t = extract_text_from_pdf(path)
    t = clean_text(t)
    return (t,extract_info(t))

#print(data_flow(resume_path)[0])