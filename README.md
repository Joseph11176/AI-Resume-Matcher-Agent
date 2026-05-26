# AI Resume Matcher Agent

AI Resume Matcher Agent is an LLM-powered recruiter assistant built for AI Marathon 2026 under the **Intelligent Recruiter** track.

The system helps recruiters analyze job descriptions and candidate resumes by ranking candidates, identifying strengths and missing skills, generating interview questions, and producing recruiter-ready candidate pitches.

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

## Features

- Upload multiple resume PDF files
- Paste a job description
- Extract text from PDF resumes
- Analyze candidate suitability using Gemini API
- Rank candidates by match score
- Generate candidate summary
- Identify candidate strengths
- Identify missing skills or gaps
- Generate suggested interview questions
- Generate recruiter pitch
- Fallback to local rule-based recruiter agent when API quota is unavailable

## Tech Stack

- Python
- Streamlit
- Gemini API
- Google GenAI SDK
- PyPDF2
- python-dotenv

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
