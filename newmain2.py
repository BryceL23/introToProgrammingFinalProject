# sources: https://www.geeksforgeeks.org/writing-excel-sheet-using-python/


############## open website with selenium and webdriver ###################
from time import sleep
import xlwt
from xlwt import Workbook
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# scrape page
URL = 'https://www.pro-football-reference.com/years/2022/rushing.htm'

chrome_driver = "Code\Projects\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.get(URL)
sleep(5)
# spans = driver.find_element(By.TAG_NAME, "span")
# print(type(spans))
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
