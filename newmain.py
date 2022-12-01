# look at scrap.py 
# look at PDFextract.py in his code (look at links in the source code) geeks for geeks writing to an excel sheet 

import requests, bs4
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

print(noStarchSoup)