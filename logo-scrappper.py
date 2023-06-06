import os
import requests
import re
from urllib import request
import json

from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def wait_till_page_load(wait_count=0):
    try:
        WebDriverWait(driver, 18).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'googleapis')]")))
        driver.implicitly_wait(2)
        # print(element.text)
        return True
    except TimeoutException:
        if wait_count != 5:
            # driver.refresh()
            return wait_till_page_load(wait_count + 1)
        else:
            return False


def is_same_team_in_config(teamName, shortName):
    for team in teamConfig:
        if team['shortName'] == shortName and team['teamName'] == teamName:
            return True
    return False


apiUrl = 'https://algs.tas.gg/api/match/<matchId>/?showBracketLink'
startMatchId = 1562    # 1562
endMatchId = 1611  # 1611
# startMatchId = 1569
# endMatchId = 1569

teamId = 1
teamConfig = []

regex = r"(\S+ [0-9]+)(,|\Z| )"

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.add_argument("--headless")
driver = webdriver.Firefox(options=fireFoxOptions)

for matchId in range(startMatchId, endMatchId+1):
    url = apiUrl.replace('<matchId>', str(matchId))
    # print(url)
    response = requests.get(url)
    points = response.text.split('---')[1].split('----')[0]
    bracketUrl = response.text.split('Bracket: ')[1]
    # print(points)
    # print(bracketUrl)
    matches = re.findall(regex, points)
    # print(matches)
    # print(len(matches))
    driver.get(bracketUrl)
    wait_result = wait_till_page_load()

    if wait_result:
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        teamElements = soup.select('div[class*="TeamInfoHeader"]')
        # print(len(teamElements))
        if len(matches) == len(teamElements):
            for index, teamElement in enumerate(teamElements):
                imageElement = teamElement.find('img')
                teamName = imageElement.parent.find('span').text
                shortName = matches[index][0].split(' ')[0]
                path = 'src/images/' + str(teamId) + '.png'
                # print(imageElement['src'])
                # print(teamName)
                # print(shortName)
                # print(path)
                if not is_same_team_in_config(teamName, shortName):
                    teamConfig.append({
                        'teamId': teamId,
                        'teamName': teamName,
                        'shortName': shortName,
                        'path': path,
                    })
                    teamId = teamId + 1
                    # print(os.path.isfile(path))
                    if not os.path.isfile(path):
                        resource = request.urlopen(imageElement['src'])
                        os.makedirs(os.path.dirname(path), exist_ok=True)
                        output = open(path, 'wb')
                        output.write(resource.read())
                        output.close()
                        file = Image.open(path)
                        file.thumbnail((64, 64), Image.Resampling.LANCZOS)
                        file.save(path)

driver.close()

# print(teamConfig)

with open("teamConfig.json", "w") as teamConfigFile:
    json.dump(teamConfig, teamConfigFile, indent=4, ensure_ascii=False, sort_keys=True)
