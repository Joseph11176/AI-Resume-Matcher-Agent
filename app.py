import os
import json
import re
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from google import genai
from google.genai.errors import ClientError

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI Resume Matcher Agent", layout="wide")


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text.strip()


def basic_keyword_score(job_description, resume):
    def clean_text(text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text

    jd_words = set(clean_text(job_description).split())
    resume_words = set(clean_text(resume).split())

    if not jd_words or not resume_words:
        return 0

    matched_words = jd_words.intersection(resume_words)
    score = int((len(matched_words) / len(jd_words)) * 100)

    return min(score, 100)

def fallback_agent_analysis(job_description, resume_text, candidate_name):
    score = basic_keyword_score(job_description, resume_text)

    resume_lower = resume_text.lower()

    strengths = []
    if "python" in resume_lower:
        strengths.append("Has Python programming knowledge relevant to technical roles.")
    if "linux" in resume_lower or "kali" in resume_lower:
        strengths.append("Has Linux or cybersecurity tool exposure.")
    if "security" in resume_lower or "penetration" in resume_lower:
        strengths.append("Shows cybersecurity-related experience or interest.")
    if "sql" in resume_lower:
        strengths.append("Has database or SQL-related knowledge.")
    if "project" in resume_lower:
        strengths.append("Has project experience that can be discussed during screening.")

    if not strengths:
        strengths = [
            "The resume contains some relevant experience for further screening.",
            "The candidate profile can be reviewed based on transferable skills.",
            "The candidate may be suitable depending on interview performance."
        ]

    missing_skills = [
        "Some technical requirements from the job description may need to be verified.",
        "Hands-on work experience should be confirmed during the interview."
    ]

    return {
        "candidate_name": candidate_name,
        "match_score": score,
        "summary": "This candidate was analyzed using the fallback recruiter agent because the LLM API quota was unavailable.",
        "strengths": strengths[:5],
        "missing_skills": missing_skills,
        "why_this_person": f"{candidate_name} is recommended based on resume-to-job matching logic and keyword overlap with the job description.",
        "interview_questions": [
            "Can you describe a project that is most relevant to this job role?",
            "What tools or technologies have you used that match this job description?",
            "Which skills from the job description do you feel most confident in?"
        ],
        "recruiter_pitch": f"{candidate_name} appears to be a potential fit based on extracted resume content and matching logic. The recruiter should review this candidate further during screening."
    }

def extract_json_from_text(text):
    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)


def analyze_candidate_with_gemini(job_description, resume_text, candidate_name):
    prompt = f"""
You are an AI Recruiter Agent.

Your task is to evaluate a candidate resume against a job description.

Job Description:
{job_description}

Candidate Name:
{candidate_name}

Candidate Resume:
{resume_text}

Return your answer strictly in valid JSON format using this structure:

{{
  "candidate_name": "{candidate_name}",
  "match_score": 0,
  "summary": "",
  "strengths": [],
  "missing_skills": [],
  "why_this_person": "",
  "interview_questions": [],
  "recruiter_pitch": ""
}}

Rules:
- match_score must be a number from 0 to 100.
- strengths must contain 3 to 5 points.
- missing_skills must contain 2 to 5 points.
- interview_questions must contain 3 questions.
- recruiter_pitch should be written for a recruiter or hiring manager.
- Do not invent experience that is not found in the resume.
- Be clear and practical.
- Return JSON only. Do not include markdown.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        result_text = response.text

    except ClientError as e:
        st.warning("Gemini quota is unavailable, so the app is using fallback demo agent analysis.")
        return fallback_agent_analysis(job_description, resume_text, candidate_name)

    except Exception as e:
        st.warning("Gemini request failed, so the app is using fallback demo agent analysis.")
        return fallback_agent_analysis(job_description, resume_text, candidate_name)

    try:
        return extract_json_from_text(result_text)
    except Exception:
        return fallback_agent_analysis(job_description, resume_text, candidate_name)

st.title("AI Resume Matcher Agent")
st.write("A Gemini-powered recruiter agent that ranks candidates based on a job description and uploaded resumes.")

st.header("1. Job Description")
job_description = st.text_area("Paste the job description here", height=220)

st.header("2. Upload Candidate Resumes")
uploaded_resumes = st.file_uploader(
    "Upload resume PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

analyze_button = st.button("Analyze Candidates with Gemini Agent")

if analyze_button:
    if not os.getenv("GEMINI_API_KEY"):
        st.error("GEMINI_API_KEY is missing. Please add it inside your .env file.")
    elif not job_description.strip():
        st.warning("Please enter a job description.")
    elif not uploaded_resumes:
        st.warning("Please upload at least one resume PDF.")
    else:
        st.subheader("Gemini Agent Analysis Result")

        results = []

        with st.spinner("Gemini Recruiter Agent is analyzing candidates..."):
            for uploaded_file in uploaded_resumes:
                resume_text = extract_text_from_pdf(uploaded_file)

                if not resume_text:
                    st.warning(f"Could not extract text from {uploaded_file.name}.")
                    continue

                analysis = analyze_candidate_with_gemini(
                    job_description=job_description,
                    resume_text=resume_text,
                    candidate_name=uploaded_file.name
                )

                analysis["resume_text"] = resume_text
                results.append(analysis)

        results = sorted(results, key=lambda x: x.get("match_score", 0), reverse=True)

        for rank, result in enumerate(results, start=1):
            st.markdown(f"## Rank {rank}: {result.get('candidate_name', 'Candidate')}")
            st.metric("Match Score", f"{result.get('match_score', 0)}%")

            st.markdown("### Candidate Summary")
            st.write(result.get("summary", ""))

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Strengths")
                for item in result.get("strengths", []):
                    st.write(f"- {item}")

            with col2:
                st.markdown("### Missing Skills / Gaps")
                for item in result.get("missing_skills", []):
                    st.write(f"- {item}")

            st.markdown("### Why This Person?")
            st.write(result.get("why_this_person", ""))

            st.markdown("### Suggested Interview Questions")
            for i, question in enumerate(result.get("interview_questions", []), start=1):
                st.write(f"{i}. {question}")

            st.markdown("### Recruiter Pitch")
            st.info(result.get("recruiter_pitch", ""))

            with st.expander("View Extracted Resume Text"):
                st.write(result.get("resume_text", ""))

            st.divider()