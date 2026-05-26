import streamlit as st
import re
from PyPDF2 import PdfReader

st.set_page_config(page_title="AI Resume Matcher Agent", layout="wide")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

def calculate_match_score(job_description, resume):
    jd_words = set(clean_text(job_description).split())
    resume_words = set(clean_text(resume).split())

    if not jd_words or not resume_words:
        return 0, []

    matched_words = jd_words.intersection(resume_words)
    score = int((len(matched_words) / len(jd_words)) * 100)

    return score, list(matched_words)

st.title("AI Resume Matcher Agent")
st.write("Upload a job description and candidate resumes to find the best match.")

st.header("1. Job Description")
job_description = st.text_area("Paste the job description here", height=200)

st.header("2. Upload Candidate Resumes")
uploaded_resumes = st.file_uploader(
    "Upload resume PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Analyze Candidates"):
    if not job_description.strip():
        st.warning("Please enter a job description.")
    elif not uploaded_resumes:
        st.warning("Please upload at least one resume PDF.")
    else:
        st.subheader("Analysis Result")

        results = []

        for uploaded_file in uploaded_resumes:
            resume_text = extract_text_from_pdf(uploaded_file)
            score, matched_words = calculate_match_score(job_description, resume_text)

            results.append({
                "name": uploaded_file.name,
                "score": score,
                "matched_words": matched_words,
                "resume_text": resume_text
            })

        results = sorted(results, key=lambda x: x["score"], reverse=True)

        for rank, result in enumerate(results, start=1):
            st.markdown(f"### Rank {rank}: {result['name']}")
            st.write(f"**Match Score:** {result['score']}%")

            st.write("**Why this person?**")
            if result["matched_words"]:
                st.write(
                    "This candidate is recommended because their resume contains skills and keywords related to the job description, such as: "
                    + ", ".join(result["matched_words"][:15])
                    + "."
                )
            else:
                st.write("This candidate has limited keyword overlap with the job description.")

            st.write("**Suggested Interview Questions:**")
            st.write("1. Can you explain your experience related to this job role?")
            st.write("2. Which project best demonstrates your technical skills?")
            st.write("3. What skills would you improve before joining this role?")

            with st.expander("View extracted resume text"):
                st.write(result["resume_text"])

            st.divider()