# # look at scrap.py 
# # look at PDFextract.py in his code (look at links in the source code) geeks for geeks writing to an excel sheet 

# import requests, bs4
# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(noStarchSoup))

# print(noStarchSoup)

############## open website with selenium and webdriver ###################
import requests, bs4

URL = 'https://www.pro-football-reference.com/years/2022/rushing.htm'

# get info from website
res = requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(soup))
print(soup)
elem = soup.select('tbody')
print(len(elem))
print(str(elem))
# dump into excel