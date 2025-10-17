# Smart Resume Screener

## What is this?

This project is a **Smart Resume Screener** that automatically analyzes resumes and evaluates how well they match a job description.  
It’s like a mini “AI recruiter” — it reads a resume, extracts skills, education, and experience, and provides a score showing how good a fit the candidate is for a specific job.

---

## How it works (Architecture / Flow)

1. **Resume Extraction**  
   - Extracts text from PDF resumes using **PyPDF2**.  
   - Cleans the text by removing extra spaces and unwanted characters.

2. **Info Extraction**  
   - Pulls out key information:  
     - **Email and phone number** (via regex)  
     - **Skills** (matches against a list of ~500 common skills)  
     - **Education** (keywords like B.Tech, Master, University)  
     - **Experience** (keywords like intern, developer, engineer)

3. **Semantic Matching**  
   - Compares the resume text with a **job description**.  
   - Uses **SentenceTransformers** (`all-MiniLM-L6-v2`) to create embeddings and compute **cosine similarity**.  
   - The similarity score indicates how closely the resume matches the job description.

4. **Score Interpretation**  
   - Converts the similarity score into human-friendly terms:  
     - 80–100% → **Excellent Fit**  
     - 60–80% → **Good Fit**  
     - 40–60% → **Average Fit**  
     - <40% → **Poor Fit**

---

## Tech Stack / Libraries Used

- **Python** – main programming language  
- **PyPDF2** – for PDF text extraction  
- **re (Regex)** – to find emails, phone numbers, and keywords  
- **SentenceTransformers** – to create semantic embeddings and compute similarity  
- **PyTorch** – backend for SentenceTransformers  
- **skills_list.py** – a custom list of 500+ skills to check against resumes  

---

## How to Use

1. Place the resume PDF you want to evaluate in a folder.  
2. Update the path to the resume in `llm_use_clean.py`.  
3. Run the script:
```bash
python llm_use_clean.py
