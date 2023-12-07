from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

#browser = webdriver.Chrome("chromedriver.exe")
#browser.get(START_URL)

page = requests.get(START_URL)
soup = bs(page.text, "html.parser")
star_table = soup.find_all("table", {"class":"wikitable sortable"})
total_table = len(star_table)
print(total_table)
temp_list = []
table_rows = star_table[1].find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
star_names = []
distance = []
mass = []
radius = []
print(temp_list)
for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
headers = ["star_name", "distance", "mass", "radius"]
df_2 = pd.DataFrame(list(zip(star_names, distance, mass, radius)), columns = ["star_name", "distance", "mass", "radius"])
print(df_2)
df_2.to_csv("dwarf_star_csv", index = True, index_label = "id")
