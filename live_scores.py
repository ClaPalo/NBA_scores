import os
import time
import isodate
import pyfiglet
from rich.console import Console
from nba_api.live.nba.endpoints import scoreboard


colors = {
    "GSW": "#1D428A",
    "LAL": "#552583",
    "DEN": "#FEC524",
    "UTA": "#002B5C",
    "BOS": "#007A33",
    "MIA": "#98002E",
    "MIL": "#00471B",
    "TOR": "#CE1141",
    "PHI": "#C4CED4",
    "BKN": "#FFFFFF",
    "IND": "#002D62",
    "ORL": "#0077C0",
    "DET": "#C8102E",
    "CHA": "#1D1160",
    "CHI": "#CE1141",
    "NYK": "#006BB6",
    "CLE": "#860038",
    "ATL": "#E03A3E",
    "WAS": "#002B5C",
    "PHX": "#E56020",
    "SAC": "#5A2D81",
    "POR": "#E03A3E",
    "MIN": "#0C2340",
    "MEM": "#5D76A9",
    "SAS": "#C4CED4",
    "NOP": "#0C2340",
    "OKC": "#007AC1",
    "HOU": "#CE1141",
    "DAL": "#00538C",
    "LAC": "#C8102E"
}

period_suffix = {
    0: "Pregame",
    1: "1st",
    2: "2nd",
    3: "3rd",
    4: "4th"
}

console = Console()

# games is an array containing dictionaries with the following structure:
# {
#     "team1": string,
#     "score1": int,
#     "team2": string,
#     "score2": int,
#     "time": string
# }


def fix_time(time):
    if time < 10:
        return "0" + str(time)
    else:
        return str(time)


def print_scores(games):
    # Pulisci lo schermo del terminale
    os.system('cls' if os.name == 'nt' else 'clear')

    # Posiziona il cursore al punto desiderato
    # Questo codice posiziona il cursore in alto a sinistra del terminale
    print("\033[1;1H", end="")

    # Stampa il numero
    for game in games:
        print_score(game["team1"], game["score1"],
                    game["team2"], game["score2"], game["time"])


# Stampa il punteggio di un game
def print_score(team1, score1, team2, score2, time):
    try:
        color1 = colors[team1]
    except KeyError:
        color1 = "blue"

    try:
        color2 = colors[team2]
    except KeyError:
        color2 = "red"

    team1 = pyfiglet.figlet_format(
        team1 + " " + str(score1), font="ansi_regular")
    team2 = pyfiglet.figlet_format(
        team2 + " " + str(score2), font="ansi_regular")

    time = pyfiglet.figlet_format(time, font="ansi_regular")

    console.print(team1, style=color1)
    console.print(time, style="white")
    console.print(team2, style=color2)


while True:
    games = scoreboard.ScoreBoard().games.get_dict()
    my_games = []
    for game in games:
        res = {}
        if game["gameClock"] != "":
            duration = isodate.parse_duration(game["gameClock"])

            # Extract components
            minutes = fix_time(duration.seconds // 60)
            seconds = fix_time(duration.seconds % 60)
        else:
            minutes = "00"
            seconds = "00"

        period = period_suffix[game["period"]
                               ] if game["period"] in period_suffix else "OT"
        res = {
            "team2": game["homeTeam"]["teamTricode"],
            "score2": game["homeTeam"]["score"],
            "team1": game["awayTeam"]["teamTricode"],
            "score1": game["awayTeam"]["score"],
            "time": minutes + ":" + seconds + " " + period
        }
        # If any of the values is empty, don't append the game to the list
        if res["team1"] != "" and res["team2"] != "":
            if game["gameStatusText"] == "Final":
                res["time"] = "Final"
            my_games.append(res)
    print_scores(my_games)
    time.sleep(5)
