from config import DEFAULT_RESUME_PATH, DEFAULT_TEAMS_CSV
from extractor import extract_text_from_pdf, load_teams_from_csv
from teamMatcher import match_resume_to_team

def main(resume_path=DEFAULT_RESUME_PATH, teams_csv_path=DEFAULT_TEAMS_CSV):
    print("Reading team data from CSV...")
    teams_df, error = load_teams_from_csv(teams_csv_path)
    if error:
        print(error)
        return

    print("Extracting text from the resume...")
    resume_text = extract_text_from_pdf(resume_path)
    if resume_text.startswith("Error"):
        print(resume_text)
        return

    print("Matching resume with teams using Gemini...")
    matching_result = match_resume_to_team(resume_text, teams_df)

    print("\nAgent Output:")
    if isinstance(matching_result.get("recommended_teams"), list):
        for result in matching_result["recommended_teams"]:
            print(f"Recommended Team: {result.get('team_name', 'N/A')}")
            print(f"Reasoning: {result.get('reasoning', 'N/A')}\n---")
    else:
        print("Error: Unexpected JSON structure.", matching_result)

if __name__ == "__main__":
    main()
