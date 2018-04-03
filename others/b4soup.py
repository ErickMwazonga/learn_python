import requests
from bs4 import BeautifulSoup
import cgi

def wr_scrape():
 import pdb
 r = requests.get('http://www.officialworldgolfranking.com/rankings/default.spssoup = BeautifulSoup(r.text)
 tables = soup.find_all('table', title="Click on player names to be taken to their individual tournaments page")
 table = tables[1]
 for info in table.contents:
   try:
     data = info.contents[7]
     player_name = data.a.string
     player_url = data.a['href']
     qs = cgi.parse_qs(data.a['href'])
     player_rank = qs['Rank'][0]
     player_ID = qs['/players/bio.sps?ID'][0]
     print '%s, %s, %s' % (player_name, player_rank, player_ID)
   except AttributeError: # incase it's just a string
     pass
   except IndexError: #this is if there is no [7]
     pass

wr_scrape()
