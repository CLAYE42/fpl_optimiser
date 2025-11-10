import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_FOOTBALL_KEY")

BASE_URL = "https://v3.football.api-sports.io"
HEADERS = {"x-apisports-key": API_KEY}

#test
response = requests.get(f"{BASE_URL}/leagues", headers=HEADERS)
data = response.json()
print(data)

# --- Basic Client Functions ---


def get_leagues():
    """Fetch available leagues."""
    url = f"{BASE_URL}/leagues"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_fixtures(league_id, season, next_matches=10):
    """Get upcoming fixtures for a league."""
    url = f"{BASE_URL}/fixtures"
    params = {"league": league_id, "season": season, "next": next_matches}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def get_team_players(team_id, season):
    """Get all players for a team in a given season."""
    url = f"{BASE_URL}/players"
    params = {"team": team_id, "season": season}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def get_player_stats(player_id, season):
    """Get detailed stats for a single player."""
    url = f"{BASE_URL}/players"
    params = {"id": player_id, "season": season}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def check_api_status():
    """Simple call to verify your API key works."""
    url = f"{BASE_URL}/status"
    response = requests.get(url, headers=HEADERS)
    return response.json()