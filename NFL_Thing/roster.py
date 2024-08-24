"""
Will create data folder and batch of .json files to create a list of players, and their teams.
"""

import os
import sys
import requests
import json

# Constants
TEAM_API = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"

def fetch_team_data(output_dir):
    # Fetch the team data from the ESPN API
    response = requests.get(TEAM_API)
    response.raise_for_status()
    data = response.json()

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over the teams and fetch their rosters
    for team in data.get("sports", [])[0].get("leagues", [])[0].get("teams", []):
        team_id = team["team"]["id"]
        team_url = f"{TEAM_API}/{team_id}?enable=roster"
        
        # Fetch the roster for each team
        team_response = requests.get(team_url)
        if team_response.status_code == 200:
            with open(os.path.join(output_dir, f"{team_id}.json"), "w") as f:
                f.write(team_response.text)
        else:
            print(f"Failed to fetch data for team ID: {team_id}")

    # Compile all team rosters into one JSON file
    compile_roster_data(output_dir)

def compile_roster_data(output_dir):
    roster = []

    for file_name in os.listdir(output_dir):
        if file_name.endswith(".json") and file_name != "roster.json":
            with open(os.path.join(output_dir, file_name), "r") as f:
                team_data = json.load(f)
                team_abbreviation = team_data["team"]["abbreviation"]
                for athlete in team_data["team"]["athletes"]:
                    roster.append({
                        "id": athlete["id"],
                        "team": team_abbreviation,
                        "position": athlete["position"]["abbreviation"],
                        "fullName": athlete["fullName"]
                    })

    # Save compiled roster data to a single JSON file
    with open(os.path.join(output_dir, "roster.json"), "w") as f:
        json.dump(roster, f, indent=2)

    # Print the compiled roster
    print(json.dumps(roster, indent=2))

if __name__ == "__main__":
    # Check if the output directory is provided
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    else:
        output_dir = "data"  # Default output directory

    fetch_team_data(output_dir)
