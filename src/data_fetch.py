import pandas as pd
from api.football_client import get_fixtures, get_team_players, check_api_status

def verify_api():
    status = check_api_status()
    print("✅ API Status Check:")
    print(status)

def fetch_fixtures(league_id=39, season=2025):
    """Fetch upcoming fixtures (default: Premier League)."""
    data = get_fixtures(league_id, season)
    fixtures = data.get("response", [])
    print(f"Found {len(fixtures)} fixtures")
    if fixtures:
        df = pd.json_normalize(fixtures)
        df.to_csv("data/fixtures.csv", index=False)
        print(f"✅ Saved {len(df)} fixtures to data/fixtures.csv")
    else:
        print("⚠️ No fixtures found. Check league_id or season.")

def fetch_team_players(team_id=50, season=2025):
    """Fetch all players for Man City (default)."""
    data = get_team_players(team_id, season)
    players = data.get("response", [])
    print(f"Found {len(players)} players")
    if players:
        df = pd.json_normalize(players)
        df.to_csv("data/players.csv", index=False)
        print(f"✅ Saved {len(df)} players to data/players.csv")
    else:
        print("⚠️ No players found. Check team_id or season.")

if __name__ == "__main__":
    # Run verification first
    verify_api()
    # Fetch sample data
    fetch_fixtures()
    fetch_team_players()