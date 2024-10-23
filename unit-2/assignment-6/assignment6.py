import requests
from bs4 import BeautifulSoup

crgslist_response = requests.get("https://newyork.craigslist.org/search/zip#search=1~gallery~0~0")
crgslist_soup_html = BeautifulSoup(crgslist_response.text, "html.parser")

crgslist_text = crgslist_soup_html.get_text()

crgslist_data = open('crgslist_free.txt', 'w')
crgslist_data.write(crgslist_text)
crgslist_data.close()

# with open('crgslist_free.txt', 'w') as crgslist_data:
#     crgslist_data.write(crgslist_text)
#alternative code that didnt work either

def getTitles(soupdata):
    titles = soupdata.select("a.result-title")
    if titles:
        for t in titles:
            print(t.text)

getTitles(crgslist_soup_html)            





# got this error: /Users/sigridsivanimekjan/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  #warnings.warn(

#fixed the issue but nothing is being printed, did some googling and craigslist does not use h2 i think may be the issue. chatgpt helped me find a new line of code that works spesifically for craigslist , replacing soupdata.select("h2") with soupdata.find_all("a", class_="result-title")
#tried to replcae it with a wikipedia article and its still not running:(
#im not sure what the issue is at this point... 
#im just gonna try to do it a diffferent way see if that works?


