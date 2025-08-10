import os
import google.generativeai as genai

# Configure Google API Key
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    print("Error: The GOOGLE_API_KEY environment variable is not set.")
    print("Please set it before running the script.")
    exit()

# Paths (optional defaults)
DEFAULT_RESUME_PATH = "Disha_Timbadiya_030.pdf"
DEFAULT_TEAMS_CSV = "TeamDetails.csv"
