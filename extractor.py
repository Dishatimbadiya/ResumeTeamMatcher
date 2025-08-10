import fitz
import pandas as pd
import os

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    if not os.path.exists(pdf_path):
        return f"Error: The file '{pdf_path}' does not exist."

    try:
        doc = fitz.open(pdf_path)
        return "".join(page.get_text() for page in doc)
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def load_teams_from_csv(csv_path):
    """Loads team data from a CSV file into a DataFrame."""
    if not os.path.exists(csv_path):
        return None, f"Error: The file '{csv_path}' does not exist."

    try:
        teams_df = pd.read_csv(csv_path)
        return teams_df, None
    except Exception as e:
        return None, f"Error reading CSV file: {e}"
