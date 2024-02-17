from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.static import teams
import isodate

nuggets = teams.find_team_by_abbreviation("DEN")
# print(nuggets)

# Today's Scoreboard
games = scoreboard.ScoreBoard().games.get_dict()
# print(games)

my_games = []

for game in games:
    # print(game["homeTeam"]["teamTricode"])
    res = {
        "team1": game["homeTeam"]["teamTricode"],
        "score1": game["homeTeam"]["score"],
        "team2": game["awayTeam"]["teamTricode"],
        "score2": game["awayTeam"]["score"],
        "time": game["gameClock"],
        "status": game["gameStatusText"],
        "period": game["period"]
    }

    my_games.append(res)

print(my_games)
