# ResumeTeamMatcher
# Resume-to-Team Matching Agent

This project uses **Google Gemini AI** to match a candidate's resume with the most suitable team(s) in a company based on provided team descriptions.  
It extracts text from the candidate's PDF resume, compares it with the provided company teams list, and recommends the best fit with reasoning.

---

## 📂 Project Structure

- .
- ├── config.py # Configuration and API key setup
- ├── extractor.py # PDF and CSV data extraction
- ├── matcher.py # AI matching logic using Gemini
- ├── main.py # Orchestration script
- ├── resume.pdf # resume
- ├── TeamDetails.csv # company's team details CSV file
- └── README.md # Project documentation

## 🛠 Prerequisites

- Python 3.8+
- A Google API key with access to the **Gemini API** ([Get API Key](https://aistudio.google.com/))
- Required Python libraries:
  ```bash
  pip install PyMuPDF pandas google-generativeai
    ```

## 📂 Data Preparation
- Before running the project, create a folder named data in the project root and place:
1. Resume PDF — Your resume file (e.g., resume.pdf)
2. Company Teams CSV — A CSV file containing team details in the following format:

```bash
Org,Subteam,Teamwork
Cloud, Cloud Infrastructure,Responsible for designing and maintaining core cloud infrastructure.
AI, AI Research,Focuses on building and deploying AI models.
Security, Cloud Security,Manages company-wide security protocols and compliance.
```

### Set your Google API key:

```bash
On Windows (PowerShell):
setx GOOGLE_API_KEY "your_api_key_here"
```

### Install dependencies:

```bash
pip install -r requirements.txt
```
🚀 Running the Project

### Run the main script:

```bash
python main.py
```

## 📝 Output Example

Step 1: Reading team data from CSV...
Step 2: Extracting text from the resume...
Step 3: Matching resume with teams using Gemini...

``` bash
Agent Output
Recommended Team: AI Research
Reasoning:
The candidate has experience in machine learning, NLP, and AI projects, aligning with AI Research goals.
---
Recommended Team: Cloud Infrastructure
Reasoning:
Background in distributed systems and cloud deployments aligns with infrastructure needs.
---
```

## 📌 Notes
1. Ensure your resume and company details CSV are inside the /data folder before running.
2. The Gemini API may sometimes return incomplete JSON — the script includes error handling to manage this.

