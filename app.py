import streamlit as st
import os
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from job_matcher import calculate_similarity
from utils import extract_skills, clean_text

# Set page configuration
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠", layout="wide")

# Add a title and a description
st.title("🧠 AI Resume Analyzer")
st.write("Upload your resumes and paste the job description to analyze the match.")

# Create a sidebar for additional options
st.sidebar.header("Options")
st.sidebar.write("Upload resumes and job description here.")

# File uploader for resumes
uploaded_files = st.sidebar.file_uploader("Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

# Text area for job description
job_description = st.sidebar.text_area("Paste Job Description Here")

# Button to trigger analysis
if st.sidebar.button("Analyze"):
    if not uploaded_files:
        st.sidebar.error("Please upload at least one resume.")
    elif not job_description.strip():
        st.sidebar.error("Please enter a job description.")
    else:
        resume_texts = []
        resume_names = []

        for file in uploaded_files:
            if file.name.endswith(".pdf"):
                text = extract_text_from_pdf(file)
            else:
                text = extract_text_from_docx(file)
            text_cleaned = clean_text(text)
            resume_texts.append(text_cleaned)
            resume_names.append(file.name)

        scores = calculate_similarity(resume_texts, clean_text(job_description))

        results = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)

        # Display results in a more attractive way
        st.subheader("📈 Matching Results:")
        for name, score in results:
            st.write(f"**{name}**: {round(score * 100, 2)}% match")

# Add a footer
st.sidebar.markdown("---")
st.sidebar.write("KARAN S MEVADA")
st.sidebar.write("[GitHub](https://github.com/iamkaran2026) | [LinkedIn](https://www.linkedin.com/in/karan-mevada-19745527b/)")