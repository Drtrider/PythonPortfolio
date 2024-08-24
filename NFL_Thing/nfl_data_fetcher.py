"""
Purpose of nfl_data_fetcher.py is to be able to fetch some player data.

PRE-REQ: You'll need to generate a roster.json using NFL_Thing\roster.py
"""

import pandas as pd
import json


def load_stats_dataframe(path_to_json):
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


# Pick which players to lookup

# Lookup batch of players player's stats

# Return some type of reccomendation on which players to pick? 