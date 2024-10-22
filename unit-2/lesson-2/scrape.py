# import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

SJM_response = requests.get("https://en.wikipedia.org/wiki/Sarah_J._Maas")
# phil_response = requests.get("https://www.newschool.edu/lang/philosophy/")

# print(response.text[:500])

SJM_soup_html = BeautifulSoup(SJM_response.text, "html.parser")
# phil_soup_html = BeautifulSoup(phil_response.text, "html.parser")

SJM_soup_text = SJM_soup_html.get_text()
# phil_soup_text = phil_soup_html.get_text()

SJM_data = open('SJM-wikipedia.txt', 'w')
SJM_data.write(SJM_soup_text)
SJM_data.close()

# phil_data = open('newschool-phil.txt', 'w')
# phil_data.write(phil_soup_text)
# phil_data.close()


def getTitles(soupdata):  
  titles = soupdata.select("h2")
  if titles:
    for t in titles:
      print(t.text)
      
print("SJM........")
getTitles(SJM_soup_html)
# print("Philosophy.........")
# getTitles(phil_soup_html)