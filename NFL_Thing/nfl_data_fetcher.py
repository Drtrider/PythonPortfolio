"""
Purpose of nfl_data_fetcher.py is to be able to fetch some player data.

PRE-REQ: You'll need to generate a roster.json using NFL_Thing\roster.py
"""

#######################
# Still to do
#######################

# Deliverable #1: Suggest a list of players for the initial draft

# Deliverable #2: Suggest players for each week

################################
################################


import pandas as pd
import json


def create_stats_dataframe(path_to_json):
    """
    Loads a .json player stats file into a pandas DataFrame.

    This function reads a JSON file containing player statistics, normalizes the data into a flat table format using `pandas.json_normalize`,
    and returns it as a DataFrame.

    Parameters:
    ----------
    path_to_json : str
        The file path to the .json file containing player stats.

    Returns:
    -------
    pd.DataFrame
        A pandas DataFrame containing the normalized player statistics.

    Raises:
    ------
    FileNotFoundError
        If the specified file does not exist.
    JSONDecodeError
        If the file is not a valid JSON.

    Example:
    -------
    >>> df_player_stats = load_stats_dataframe('NFL_Thing/example_athlete_stats.json')
    >>> print(df_player_stats.head())
    """
    
    # Load the JSON data from a file
    with open(path_to_json) as f:
        data = json.load(f)
    
    # Normalize the JSON data
    df_player_stats = pd.json_normalize(data, record_path=['splits', 'categories', 'stats'], meta=[['splits', 'name'], ['categories', 'name']])

    return df_player_stats

def create_df_of_players(path_to_player_list):
    """Returns a dataframe of players, if given a roster.json"""

    # Load the JSON data from a file
    with open(path_to_player_list) as f:
        data = json.load(f)

    # Create the dataframe
    df_players = pd.json_normalize(data)

    return df_players

# Create a df of players
path_to_player_list = r"E:\Documents\Repos\PythonPortfolio-1\NFL_Thing\data\roster.json"
df_players = create_df_of_players(path_to_player_list)

# Create a dataframe of stats for first 10  players
pd.DataFrame()
for player in df_players.head(10).itertuples():
    print(f"Looking up stats for: {player.fullName}")






