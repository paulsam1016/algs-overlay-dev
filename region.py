import json
import re
import requests


def set_region(shortName, matchId):
    for team in teamConfig:
        if team['shortName'] == shortName:
            if matchId >= 1562 and matchId <= 1571:
                team['region'] = 'APAC N'
            elif matchId >= 1572 and matchId <= 1581:
                team['region'] = 'NA'
            elif matchId >= 1582 and matchId <= 1591:
                team['region'] = 'APAC S'
            elif matchId >= 1592 and matchId <= 1601:
                team['region'] = 'EMEA'
            elif matchId >= 1602 and matchId <= 1611:
                team['region'] = 'SA'


apiUrl = 'https://algs.tas.gg/api/match/<matchId>/?showBracketLink'
startMatchId = 1562    # 1562
endMatchId = 1611  # 1611
# startMatchId = 1562
# endMatchId = 1562

teamConfig = []

regex = r"(\S+ [0-9]+)(,|\Z| )"

with open("./teamConfig.json", "r") as teamConfigFile:
    teamConfig = json.load(teamConfigFile)

for matchId in range(startMatchId, endMatchId+1):
    url = apiUrl.replace('<matchId>', str(matchId))
    print(url)
    response = requests.get(url)
    points = response.text.split('---')[1].split('----')[0]
    # print(points)
    matches = re.findall(regex, points)
    # print(matches)
    # print(len(matches))
    for match in matches:
        shortName = match[0].split(' ')[0]
        set_region(shortName, matchId)

# print(teamConfig)

with open("./teamConfig.json", "w") as teamConfigFile:
    json.dump(teamConfig, teamConfigFile, indent=4, ensure_ascii=False, sort_keys=True)
