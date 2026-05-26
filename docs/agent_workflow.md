# Agent Workflow

## AI Resume Matcher Agent

This document explains the agent workflow for the AI Resume Matcher Agent project.

The system is designed for the **Intelligent Recruiter** track. It analyzes a job description and multiple candidate resume PDFs, then generates a ranked candidate report with recruiter-ready insights.

---

## Agent Framework Diagram

```text
┌────────────────────────────────────┐
│            User Input              │
│                                    │
│  - Job Description                 │
│  - Candidate Resume PDF Files      │
└──────────────────┬─────────────────┘
                   ↓
┌────────────────────────────────────┐
│        PDF Text Extraction          │
│                                    │
│  Tool: PyPDF2                      │
│  Purpose: Extract text content     │
│  from uploaded resume PDFs         │
└──────────────────┬─────────────────┘
                   ↓
┌────────────────────────────────────┐
│          Recruiter Agent            │
│                                    │
│  LLM Provider: Chutes API           │
│  Model: DeepSeek V3.2 TEE           │
│                                    │
│  Fallback: Rule-Based Agent         │
└──────────────────┬─────────────────┘
                   ↓
┌────────────────────────────────────┐
│        Agent Reasoning Steps        │
│                                    │
│  1. Job Requirement Analysis        │
│  2. Candidate Profile Analysis      │
│  3. Resume-to-Job Matching          │
│  4. Strengths Detection             │
│  5. Missing Skills Detection        │
│  6. Interview Question Generation   │
│  7. Recruiter Pitch Generation      │
└──────────────────┬─────────────────┘
                   ↓
┌────────────────────────────────────┐
│       Ranked Candidate Report       │
│                                    │
│  - Candidate Ranking                │
│  - Match Score                      │
│  - Candidate Summary                │
│  - Strengths                        │
│  - Missing Skills / Gaps            │
│  - Why This Person?                 │
│  - Suggested Interview Questions    │
│  - Recruiter Pitch                  │
└────────────────────────────────────┘
