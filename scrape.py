from bs4 import BeautifulSoup
import requests

url = "https://www.nba.com/player/1641705/victor-wembanyama/profile"

page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

nameTable = soup.find_all('tr')[0]
names = nameTable.find_all('th')[4:23]

statTable = soup.find_all('tr')[1] #Finds stats table
stats = statTable.find_all('td')[3:23] #Finds Stats

nameList = [title.text for title in names]
statList = [title.text for title in stats] #Lists the stats

print(nameList,"\n",statList)