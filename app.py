import streamlit as st
from groq import Groq
import json
import os
import re
from dotenv import load_dotenv

# ---------------------------
# Load Environment Variables 
#This code is used to safely connect your GenAI application to the Groq API, which allows you to access powerful language models.
 # First, load_dotenv() loads environment variables from a .env file. 
 # A .env file is used to store sensitive information like API keys securely, instead of writing them directly in the code.
# ---------------------------

load_dotenv()

# retrieves the Groq API key from the environment variables.

# The if not GROQ_API_KEY: block checks whether the key exists.If it is missing, Streamlit (st.error() and st.stop()) shows an error message and stops the app to prevent it from running without authentication."""

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Groq API key not found. Please set GROQ_API_KEY in .env file.")
    st.stop()

# creates a Groq client object using the API key. This client is used to send prompts to the model and receive AI-generated responses."""

client = Groq(api_key=GROQ_API_KEY)


# Streamlit Page Config 
# This sets up the Streamlit app’s basic settings like the browser tab title, page icon, and layout width.
 # It ensures the app looks professional and uses the full screen space."""

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)
# This displays the main heading and shows which AI model is being used. It helps users understand the purpose of the app and the underlying model."""

st.title("📄 AI Resume Analyzer (Groq - Free LLM)")
st.markdown("Model: llama-3.1-8b-instant")

# ---------------------------
# JSON Extraction (Robust Fix)
# This function safely extracts valid JSON from AI responses. 
# It handles cases where the model adds extra text and ensures only properly formatted JSON is processed."""
# ---------------------------
def extract_json(text):
    
    # Safely extract JSON from model output. Handles cases where model adds extra text.
    
    try:
        return json.loads(text)
    except:
        pass

    json_match = re.search(r"\{.*\}", text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except:
            return None

    return None

# ---------------------------
# Prompt Builder
# This function generates a structured prompt for the AI to evaluate how well a resume matches a job description."""
# ---------------------------
def build_prompt(resume, job_description):
    return f"""
You are a senior HR recruiter and ATS optimization expert.

Your task is to analyze how well the resume matches the job description.

Evaluation Criteria:
- Skills Match (40%)
- Experience Relevance (30%)
- Education Match (20%)
- Certifications & Extras (10%)

Provide:

1. Overall match percentage (0-100)
2. Detailed score breakdown
3. Missing critical skills
4. Specific improvement suggestions
5. Final hiring recommendation (Yes/Maybe/No)

Resume:
{resume}

Job Description:
{job_description}

IMPORTANT:
- Return ONLY valid JSON.
- Do NOT include explanations.
- Do NOT include markdown.
- Do NOT include text before or after JSON.

Return strictly in this format:

{{
    "match_percentage": number,
    "score_breakdown": {{
        "skills": number,
        "experience": number,
        "education": number,
        "certifications": number
    }},
    "missing_skills": [],
    "improvement_suggestions": [],
    "hiring_recommendation": ""
}}
"""

# ---------------------------
# LLM Call
# This function sends the generated prompt to the Groq LLM to analyze the resume. 
# It calls the model (llama-3.1-8b-instant) with temperature set to 0 for consistent JSON output."""
# ---------------------------
def analyze_resume(resume, job_description):
    prompt = build_prompt(resume, job_description)

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Updated working model
            messages=[{"role": "user", "content": prompt}],
            temperature=0,  # Critical for stable JSON
            max_tokens=1500
        )

        content = response.choices[0].message.content

        # After receiving the response, it extracts and parses the JSON using extract_json()

        parsed = extract_json(content)

        if parsed:
            return parsed
        else:
            return {
                "error": "Model did not return valid JSON",
                "raw_output": content
            }

    except Exception as e:
        return {"error": str(e)}

# ---------------------------
# UI Layout
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area("Paste Resume Here", height=400)

with col2:
    job_text = st.text_area("Paste Job Description Here", height=400)

st.divider()

if st.button("🔍 Analyze Resume", use_container_width=True):

    if not resume_text or not job_text:
        st.warning("Please provide both resume and job description.")
    else:
        with st.spinner("Analyzing resume using LLaMA 3.1..."):
            result = analyze_resume(resume_text, job_text)

        if "error" in result:
            st.error(result["error"])
            if "raw_output" in result:
                st.subheader("Raw Model Output")
                st.code(result["raw_output"])
        else:
            st.success(f"Match Score: {result['match_percentage']}%")

            st.subheader("Score Breakdown")
            st.json(result["score_breakdown"])

            st.subheader("Missing Skills")
            for skill in result["missing_skills"]:
                st.write(f"- {skill}")

            st.subheader("Improvement Suggestions")
            for suggestion in result["improvement_suggestions"]:
                st.write(f"- {suggestion}")

            st.subheader("Hiring Recommendation")
            st.info(result["hiring_recommendation"])
