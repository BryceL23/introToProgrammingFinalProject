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
searchresults = driver.find_elements(By.XPATH,"//td[contains(@class,'left')]")
searchresults1 = driver.find_elements(By.XPATH,"//td[contains(@class,'right')]")
# searchresults = driver.find_elements(By.XPATH,"//span[contains(@class,'ng-binding')]")

datafound = []
datafound1 =[]
for i in searchresults:
    if len(i.text) > 0:
        datafound.append(i.text)
    if len(datafound) > 162:
        break

for i in searchresults1:
    if len(i.text) > 0:
        datafound.append(i.text)
    if len(datafound) > 162:
        break
print(datafound)

#################### write to excel #########################
wb = Workbook()

sheet1 = wb.add_sheet("2022 Rushing Totals")


sheet1.write(0,0, "Name")
sheet1.write(0,1, "Team")
sheet1.write(0,2, "Position")
sheet1.write(0,3, "Attempts")
sheet1.write(0,4, "Yards")

for i in range(0,162):
    sheet1.write((i)//3+1,i%3, datafound[i])
# modulo takes remainder so it does i/3 the puts the remainder in that row 

for i in range(0,162):
    sheet1.write((i)//3+4,i%3, datafound1[i])
# what is added is where the column of new data input begins
wb.save('xlwt_Rushing_Totals_Data1.xls')



#it is erroring because i do not have enoiugh values