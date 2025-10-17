from sentence_transformers import SentenceTransformer, util
import torch
from resume_txt_extract import data_flow

resume_path = r"C:\Users\heman\Desktop\hemanth_resume_sep_25.pdf"
clean_text, info = data_flow(resume_path)

job_desc = """
We are looking for a Data Analyst to join our analytics team and help us make data-driven decisions across business operations.
The ideal candidate will have strong analytical skills, proficiency in data manipulation tools, and the ability to communicate insights clearly.

Responsibilities:
- Collect, clean, and analyze large datasets from multiple sources.
- Build dashboards and reports to visualize KPIs and business trends.
- Perform statistical analysis to identify patterns and correlations.
- Collaborate with business and engineering teams to define metrics and requirements.
- Automate recurring reports and data workflows.
- Present findings and actionable insights to management.

Required Skills:
- Strong knowledge of SQL, Excel, and data visualization tools (Tableau, Power BI, or similar).
- Experience with Python or R for data analysis.
- Familiarity with Pandas, NumPy, and Matplotlib.
- Understanding of statistical methods, data cleaning, and feature engineering.
- Ability to work with large structured and unstructured datasets.
- Strong communication and presentation skills.

Preferred Qualifications:
- Experience with cloud platforms (AWS, GCP, or Azure).
- Knowledge of ETL pipelines or data warehousing tools (Snowflake, BigQuery).
- Exposure to machine learning basics and predictive analytics.
- Bachelor's degree in Statistics, Computer Science, Data Science, or related field.
"""

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = SentenceTransformer('all-MiniLM-L6-v2', device=device)

resume_emb = model.encode(clean_text, convert_to_tensor=True)
jd_emb = model.encode(job_desc, convert_to_tensor=True)
score = float(util.cos_sim(resume_emb, jd_emb))

def interpret_score(score):
    pct = score * 100
    if pct >= 80:
        return "Excellent Fit"
    elif pct >= 60:
        return "Good Fit"
    elif pct >= 40:
        return "Average Fit"
    else:
        return "Poor Fit"

print("===== Resume Info Extracted =====")
print(f"Email: {info.get('email')}")
print(f"Phone: {info.get('phone')}")
print(f"Skills: {info.get('skills')}")
print(f"Education: {info.get('education')}")
print(f"Experience: {info.get('experience')}\n")

print("===== Semantic Matching =====")
print(f"Match Score: {score*100:.2f}%")
print(f"Interpretation: {interpret_score(score)}")
