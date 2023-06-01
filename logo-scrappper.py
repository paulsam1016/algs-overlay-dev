import os
import urllib
from urllib import request

from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def wait_till_page_load(wait_count=0):
    try:
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.ID, "full-standings-first-row").text != ''
        )
        return True
    except TimeoutException:
        if wait_count != 5:
            driver.refresh()
            return wait_till_page_load(wait_count + 1)
        else:
            return False


# urls = [
#     'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/north-america/leaderboard/',
#     'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/europe-middle-east-and-africa/leaderboard',
#     'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/asia-pacific-north/leaderboard/',
#     'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/asia-pacific-south/leaderboard',
#     'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/south-america/leaderboard/',
# ]

urls1 = [
    'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/north-america/leaderboard/',
    'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/europe-middle-east-and-africa/leaderboard',
    'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/asia-pacific-north/leaderboard/',
    'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/asia-pacific-south/leaderboard',
    'https://battlefy.com/apex-legends-global-series-year-3/pro-league-split-2/south-america/leaderboard/',
]

urls2 = [
    'https://algs.tas.gg/api/match/1562/',
    'https://algs.tas.gg/api/match/1572/',
    'https://algs.tas.gg/api/match/1582/',
    'https://algs.tas.gg/api/match/1592/',
    'https://algs.tas.gg/api/match/1602/',
]




fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.add_argument("--headless")
driver = webdriver.Firefox(options=fireFoxOptions)

for url in urls2:
    driver.get(url)
    print(driver.page_source)


# for url in urls:
#     driver.get(url)
#     wait_result = wait_till_page_load()
#
#     if wait_result:
#         soup = BeautifulSoup(driver.page_source, features="html.parser")
#         for row in soup.select('div[class*="ProleagueFullStandingsRow"]'):
#             for item in row.find_all('img'):
#                 print(item['alt'].split(' Logo')[0])
#                 print(item['src'])
#                 region = ''.join(word[0] for word in url.split('/')[5].split('-'))
#                 file_name = ''.join(filter(str.isalnum, item['alt'].split(' Logo')[0]))
#                 path = 'src/images/' + region + '_' + file_name + '.png'
#                 resource = request.urlopen(item['src'])
#                 os.makedirs(os.path.dirname(path), exist_ok=True)
#                 output = open(path, 'wb')
#                 output.write(resource.read())
#                 output.close()
#                 file = Image.open(path)
#                 file.thumbnail((64, 64), Image.Resampling.LANCZOS)
#                 file.save(path)
#
driver.close()

# # ProleagueFullStandingsRow
# regex = re.compile('.*ProleagueFullStandingsRow.*')
# for EachPart in soup.find_all("div", {"class": regex}):
#     print(EachPart.get_text())

# print(divs)
