# AI Resume Matcher Agent

AI Resume Matcher Agent is an LLM-powered recruiter assistant built for AI Marathon 2026 under the **Intelligent Recruiter** track.

The system helps recruiters analyze job descriptions and candidate resumes by ranking candidates, identifying strengths and missing skills, generating interview questions, and producing recruiter-ready candidate pitches.

---

## Project Overview

Traditional recruitment screening can be time-consuming because recruiters need to manually read multiple resumes and compare them with job requirements.

This project solves the problem by using an AI recruiter agent that can:

- Read a job description
- Extract text from uploaded resume PDFs
- Analyze candidate-job fit
- Rank candidates based on match score
- Generate recruiter-friendly reasoning
- Suggest interview questions
- Produce a short recruiter pitch

---

## Features

- Upload multiple resume PDF files
- Paste a job description
- Extract text from PDF resumes
- Analyze candidate suitability using Chutes API
- Use DeepSeek V3.2 TEE for LLM-based recruiter reasoning
- Rank candidates by match score
- Generate candidate summary
- Identify candidate strengths
- Identify missing skills or gaps
- Generate suggested interview questions
- Generate recruiter pitch
- Fallback to a local rule-based recruiter agent when the API is slow or unavailable

---

## Tech Stack

- Python
- Streamlit
- Chutes API
- DeepSeek V3.2 TEE
- OpenAI-compatible API client
- PyPDF2
- python-dotenv

---

## System Architecture

```text
User Input
│
├── Job Description
├── Resume PDF Files
│
▼
PDF Text Extraction
│
▼
Recruiter Agent
│
├── Chutes API
├── DeepSeek V3.2 TEE
└── Fallback Rule-Based Agent
│
▼
Agent Reasoning Steps
│
├── Job Requirement Analysis
├── Candidate Profile Analysis
├── Resume-to-Job Matching
├── Strengths Detection
├── Missing Skills Detection
├── Interview Question Generation
└── Recruiter Pitch Generation
│
▼
Ranked Candidate Report
│
├── Match Score
├── Candidate Summary
├── Strengths
├── Missing Skills
├── Why This Person?
├── Interview Questions
└── Recruiter Pitch
```

---

## Installation Step

### 1. Clone the Repository

```bash
git clone https://github.com/Joseph11176/AI-Resume-Matcher-Agent.git
```

### 2. Go to the Project Folder

```bash
cd AI-Resume-Matcher-Agent
```

### 3. Install Required Dependencies

```bash
py -m pip install -r requirements.txt
```

If `py` does not work, try:

```bash
python -m pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root directory.

```env
CHUTES_API_KEY=your_chutes_api_key_here
```

Example:

```env
CHUTES_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
```

Do not upload the `.env` file to GitHub.

Make sure `.gitignore` contains:

```gitignore
.env
__pycache__/
*.pyc
.venv/
venv/
desktop.ini
```

---

## How to Run

Run the Streamlit application:

```bash
py -m streamlit run app.py
```

If `py` does not work, try:

```bash
python -m streamlit run app.py
```

After running the command, open the local URL shown in the terminal.

Usually it will be:

```text
http://localhost:8501
```

---

## How to Use

1. Paste a job description into the **Job Description** text area.
2. Upload one or more candidate resume PDF files.
3. Click **Analyze Candidates with Chutes Agent**.
4. View the ranked candidate results.
5. Review each candidate's:
   - Match score
   - Candidate summary
   - Strengths
   - Missing skills or gaps
   - Suggested interview questions
   - Recruiter pitch

---

## Fallback Agent

If the Chutes API is slow, unavailable, or the API request fails, the system automatically uses a local rule-based recruiter agent.

The fallback agent helps the prototype continue running during live demonstration instead of crashing.

The fallback agent can still generate:

- Basic match score
- Candidate strengths
- Missing skills
- Interview questions
- Recruiter pitch

---

## Project Structure

```text
AI-Resume-Matcher-Agent/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   └── agent_workflow.md
│
└── sample_data/
    ├── job_description.txt
    ├── resume_1.txt
    └── resume_2.txt
```

---

## AI Agent Output

For each candidate, the system generates:

- Candidate ranking
- Match score
- Candidate summary
- Strengths
- Missing skills or gaps
- Explanation of why the candidate is suitable
- Suggested interview questions
- Recruiter pitch

Example output format:

```json
{
  "candidate_name": "candidate_resume.pdf",
  "match_score": 85,
  "summary": "Short candidate summary.",
  "strengths": [
    "Relevant technical skill",
    "Relevant project experience",
    "Good communication or teamwork ability"
  ],
  "missing_skills": [
    "Skill or requirement that needs further verification",
    "Area that may require improvement"
  ],
  "why_this_person": "Explanation of why this candidate is suitable.",
  "interview_questions": [
    "Question 1",
    "Question 2",
    "Question 3"
  ],
  "recruiter_pitch": "Short pitch for the recruiter or hiring manager."
}
```

---

## AI Marathon Track

This project is developed for the **Intelligent Recruiter** problem statement.

The goal is to create an agent that takes a job description and a pool of candidate data, identifies the best matches, and generates personalized reasoning for recruiters.

---

## Future Improvements

- Add vector search for more accurate resume matching
- Support DOCX resume files
- Add LinkedIn profile integration
- Add automated recruiter email generation
- Export candidate analysis as PDF report
- Add dashboard analytics for recruiters
- Improve scoring with skill weighting
- Add multi-job matching support
- Add candidate comparison table
- Add authentication for recruiter users
- Store previous analysis history

---

## Team

- Joseph Ang
