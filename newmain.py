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
from xlwt import Workbook
URL = 'https://www.pro-football-reference.com/years/2022/rushing.htm'

# get info from website
res = requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(soup))
print(soup)
# elem = soup.select('tbody')
elem = soup.select('tr' , 'tbody')
print(len(elem))
print(str(elem))

searchresults = driver.find_elements(By.XPATH,"//span[contains(@class,'ng-binding')]")

datafound = []

for i in searchresults:
    if len(i.text) > 0:
        datafound.append(i.text)
    if len(datafound) > 45:
        break

print(datafound)

# write to excel
wb = Workbook()

sheet1 = wb.add_sheet("Sheet 1")

for i in range(0,45):
    sheet1.write(1+i,0, datafound[i])

wb.save('xlwt_example.xls')

# dump into excel