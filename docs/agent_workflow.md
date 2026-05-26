┌──────────────────────────────┐
│          User Input           │
│ Job Description + Resume PDFs │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      PDF Text Extraction      │
│           PyPDF2              │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│       Recruiter Agent         │
│ Chutes API + DeepSeek V3.2    │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      Agent Reasoning Steps    │
│ - Job Requirement Analysis    │
│ - Resume Profile Analysis     │
│ - Candidate Matching          │
│ - Strengths Detection         │
│ - Missing Skills Detection    │
│ - Interview Q Generation      │
│ - Recruiter Pitch Generation  │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│     Ranked Candidate Report   │
│ - Match Score                 │
│ - Candidate Summary           │
│ - Why This Person?            │
│ - Interview Questions         │
│ - Recruiter Pitch             │
└──────────────────────────────┘
