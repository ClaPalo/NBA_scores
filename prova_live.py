import os
import time
import pyfiglet
import rich
from rich.console import Console
from rich.live import Live

team1 = "GSW"
score1 = 100
team2 = "LAL"
score2 = 99
text = f"{team1} {score1} - {team2} {score2} 08:27 4th"


def updateScore():
    global score1
    global text
    score1 = score1 + 1
    text = f"{team1} {score1} - {team2} {score2} 08:27 4th"
    time.sleep(1)


with Live(text, refresh_per_second=4) as live:
    while True:
        live.update(text)
        updateScore()
