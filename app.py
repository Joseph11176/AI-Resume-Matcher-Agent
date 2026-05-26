import streamlit as st
import re

st.set_page_config(page_title="AI Resume Matcher Agent", layout="wide")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
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
st.write("Paste a job description and candidate resumes to find the best match.")

st.header("1. Job Description")
job_description = st.text_area("Paste the job description here", height=200)

st.header("2. Candidate Resumes")
resume_1 = st.text_area("Candidate 1 Resume", height=180)
resume_2 = st.text_area("Candidate 2 Resume", height=180)
resume_3 = st.text_area("Candidate 3 Resume", height=180)

if st.button("Analyze Candidates"):
    if not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        st.subheader("Analysis Result")

        candidates = {
            "Candidate 1": resume_1,
            "Candidate 2": resume_2,
            "Candidate 3": resume_3
        }

        results = []

        for name, resume in candidates.items():
            if resume.strip():
                score, matched_words = calculate_match_score(job_description, resume)
                results.append({
                    "name": name,
                    "score": score,
                    "matched_words": matched_words,
                    "resume": resume
                })

        results = sorted(results, key=lambda x: x["score"], reverse=True)

        for rank, result in enumerate(results, start=1):
            st.markdown(f"### Rank {rank}: {result['name']}")
            st.write(f"**Match Score:** {result['score']}%")

            st.write("**Why this person?**")
            st.write(
                f"This candidate matches the job description based on shared skills and keywords such as: "
                f"{', '.join(result['matched_words'][:15]) if result['matched_words'] else 'No strong keyword match found'}."
            )

            st.write("**Suggested Interview Questions:**")
            st.write("1. Can you explain your experience related to this job role?")
            st.write("2. Which project best demonstrates your technical skills?")
            st.write("3. What skills would you improve before joining this role?")

            st.divider()