📄 AI Resume Analyzer (LLMs + Generative AI)

An AI-powered Resume Analyzer that evaluates how well a resume matches a job description using Large Language Models (LLMs). The application provides a match score, skill gap analysis, and improvement suggestions to help users optimize their resumes for better hiring chances.

The project uses Streamlit for the interface and Groq LLM (LLaMA 3.1) for intelligent resume analysis.

🚀 Features

📊 Resume vs Job Description Matching

🧠 AI-powered analysis using LLMs

📈 Match percentage scoring

🛠 Skill gap identification

💡 Resume improvement suggestions

📋 Hiring recommendation (Yes / Maybe / No)

⚡ Fast inference using Groq API

🖥 Interactive Streamlit UI

🧠 How It Works

User pastes their resume text.

User pastes the job description.

The system sends both inputs to a Large Language Model (LLaMA 3.1).

The model evaluates based on:

Skills match (40%)

Experience relevance (30%)

Education match (20%)

Certifications & extras (10%)

The model returns structured JSON containing:

Match score

Skill gaps

Suggestions

Hiring recommendation.

The prompt forces the model to return structured JSON output for consistent results. 

app

🛠 Tech Stack

Python

Streamlit

Groq API

LLaMA 3.1 LLM

Generative AI

Python-dotenv

Dependencies used in the project:

streamlit

groq

python-dotenv 

requirements

📂 Project Structure
AI-Resume-Analyzer
│
├── app.py              # Main Streamlit application
├── test.py             # API connection test script
├── requirements.txt    # Project dependencies
├── .env                # Stores Groq API key
└── README.md

Example Groq API usage is demonstrated in the test script. 

test

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Create .env File

Create a .env file in the project root:

GROQ_API_KEY=your_api_key_here

Get your API key from
https://console.groq.com

▶️ Run the Application
streamlit run app.py

The app will open in your browser.

📊 Output Example

The AI returns structured analysis like:

Match Score: 78%

Score Breakdown:
Skills: 32
Experience: 25
Education: 15
Certifications: 6

Missing Skills:
- Docker
- AWS
- System Design

Suggestions:
- Add project experience with cloud technologies
- Highlight backend API development

Hiring Recommendation:
Maybe
🎯 Use Cases

Resume optimization for job seekers

ATS compatibility checking

Career guidance tools

HR resume screening automation

🔮 Future Improvements

Resume PDF upload support

ATS keyword optimization

Resume rewriting using AI

Multiple job comparison

Dashboard analytics

👩‍💻 Author

Namratha Naik

AI / Full Stack Developer
Interested in MERN Stack, Generative AI, and Machine Learning applications.
