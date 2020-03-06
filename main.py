import json
from datetime import date
import os
import sys
from time import sleep


plataforma = sys.platform
os.startfile('.\webscreping.py')
sleep(15)

data = date.today()
data_atual = '{}/{}/{}'.format(data.day, data.month, data.year)

dados = open('ranking.json').read()
objeto = json.loads(dados)

times = {
    'ATL': "Atlanta Hawks",
    'BOS': "Boston Celtics",
    'BKN': "Brooklyn Nets",
    'CHA': "Charlotte Hornets",
    'CHI': "Chicago Bulls",
    'CLE': "Cleveland Cavaliers",
    'DAL': "Dallas Mavericks",
    'DEN': "Denver Nuggets",
    'DET': "Detroit Pistons",
    'GSW': "Golden State Warriors",
    'HOU': "Houston Rockets",
    'IND': "Indiana Pacers",
    'LAC': "LA Clippers",
    'LAL': "Los Angeles Lakers",
    'MEM': "Memphis Grizzlies",
    'MIA': "Miami Heat",
    'MIL': "Milwaukee Bucks",
    'MIN': "Minnesota Timberwolves",
    'NOP': "New Orleans Pelicans",
    'NYK': "New York Knicks",
    'OKC': "Oklahoma City Thunder",
    'ORL': "Orlando Magic",
    'PHI': "Philadelphia 76ers",
    'PHX': "Phoenix Suns",
    'POR': "Portland Trail Blazers",
    'SAC': "Sacramento Kings",
    'SAS': "San Antonio Spurs",
    'TOR': "Toronto Raptors",
    'UTA': "Utah Jazz",
    'WAS': "Washington Wizards",
}
opcoes = {
    1: "points",
    2: "assistants",
    3: "3points",
    4: "rebounds",
    5: "steals",
    6: "blocks"
}


print('\33[44mN\33[m\33[41mBA\33[m Simple Stats Table - TOP 10')
op = 1
while op != 0:
    print('Categories: ')
    print('1 - Points')
    print('2 - Assistants')
    print('3 - 3 points')
    print('4 - Rebounds')
    print('5 - Steals')
    print('6 - Blocks')
    print('0 - /Exit/')

    op = int(input('Choose your option: '))
    os.system('cls')

    if op == 1:
        jogadores = objeto[opcoes[op]]
        print(
            f'Category: \33[1;34;40mPOINTS\33[m              Updated: {data_atual}')
    elif op == 2:
        jogadores = objeto[opcoes[op]]
        print(
            f'Category: \33[1;34;40mASSISTANTS\33[m           Updated: {data_atual}')
    elif op == 3:
        jogadores = objeto[opcoes[op]]
        print(
            f'Category: \33[1;34;40m3 POINTS\33[m             Updated: {data_atual}')
    elif op == 4:
        jogadores = objeto[opcoes[op]]
        print(
            f'Category: \33[1;34;40mREBOUNDS\33[m             Updated: {data_atual}')
    elif op == 5:
        jogadores = objeto[opcoes[op]]
        print(
            f'Category: \33[1;34;40mSTEALS\33[m               Updated: {data_atual}')
    elif op == 6:
        jogadores = objeto[opcoes[op]]
        print(
            f'Category: \33[1;34;40mBLOCKS\33[m               Updated: {data_atual}')
    elif op == 0:
        print('\33[1;36mThank You. Please come again!\33[m')
        op = 0
        break
    else:
        print('\33[1;31mError: Invalid Option. Try Again!\33[m')
        op = 0
        break

    for i in range(0, 10):
        jogador = jogadores[i]
        time = jogador['team']
        print(
            f"{jogador['pos']}°    --  \33[1m{jogador['player']}\33[m  --  {times[time]}  --  \33[1;32mtotal: {jogador['total']}\33[m")
