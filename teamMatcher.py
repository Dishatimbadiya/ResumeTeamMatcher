import re
import json
import google.generativeai as genai

def match_resume_to_team(resume_text, teams_df):
    """Analyzes a resume and suggests the best-fit team(s) using Gemini."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')

        teams_list = "\n".join(
            [f"Team: {row['Subteam']}\nDescription: {row['Teamwork']}\n" 
             for _, row in teams_df.iterrows()]
        )

        prompt = (
            "You are a sophisticated AI agent for a company's HR department. "
            "Your task is to review a candidate's resume and recommend the most suitable team(s). "
            "Provide reasoning for each choice in JSON format only. "
            "The JSON must have 'recommended_teams' as an array of objects with 'team_name' and 'reasoning'. "
            "If no strong match, include one entry with 'team_name': 'No strong match'.\n\n"
            f"Here are the teams:\n{teams_list}\n\nResume:\n{resume_text}"
        )

        response = model.generate_content(prompt)
        raw_text = response.text.strip()

        json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                return {"recommended_teams": [{"team_name": "Uncertain", "reasoning": "JSON parsing failed."}]}
        else:
            return {"recommended_teams": [{"team_name": "Uncertain", "reasoning": raw_text}]}

    except Exception as e:
        return {"recommended_teams": [{"team_name": "Error", "reasoning": f"An error occurred: {e}"}]}
