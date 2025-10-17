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
    
text = extract_text_from_pdf(resume_path)
print(text)