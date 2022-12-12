# sources: 
# Links below were read and watched and used to influence the direction of the code but the final code is primarily built off of Mr. Cozort's code with modifications to fit the data values of my project 
# https://www.geeksforgeeks.org/writing-excel-sheet-using-python/
# https://www.youtube.com/watch?v=mDveiNIpqyw
# https://automatetheboringstuff.com/2e/chapter12/
# Mr. Cozort's class example code and assistance from my table mates, primarily Jonas Thieme


############## open website with selenium and webdriver ###################
from time import sleep
# import xlwt
from xlwt import Workbook
from selenium import webdriver
# allows for the webpage used in the project to be accessed and opened and closed through the software, not needing to be manually controlled
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# scrape page
URL = 'https://www.pro-football-reference.com/years/2022/rushing.htm'
# url to draw the data from for the project 

chrome_driver = "Code\Projects\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
# the driver used to control the webpages will open the url in a chrome browser
driver.get(URL)
# loads up or starts the search engine
sleep(5)
# delays the execution of the task for the amount of seconds imput into the ()

# spans = driver.find_element(By.TAG_NAME, "span")
# print(type(spans))

searchresults = driver.find_elements(By.XPATH,"//td[contains(@class,'left')]")
# defining the variable of searchrsesults which will locate the selected data from the 'left' class and store it until it is called to write it somewhere else
searchresults1 = driver.find_elements(By.XPATH,"//td[contains(@class,'right')]")
# defining the variable of searchrsesults which will locate the selected data from the 'left' class and store it until it is called to write it somewhere else

# searchresults = driver.find_elements(By.XPATH,"//span[contains(@class,'ng-binding')]")


datafound = []
# stores the list for the different sets of data 
datafound1 =[]
# stores the list for the different sets of data 

for i in searchresults:
    if len(i.text) > 0:
        datafound.append(i.text)

    if len(datafound) > 156:
        break
# gather the data within the provided source up to the determined number of string values and store them to be later written to and excel file when later called upon, the loop runs within itself until the desirved info is collected and then it breaks
for i in searchresults1:
    if len(i.text) > 0:
        datafound1.append(i.text)
    if len(datafound1) > 572:
        break
    # gather the data within the provided source up to the determined number of string values and store them to be later written to and excel file when later called upon, the loop runs within itself until the desirved info is collected and then it breaks


#################### write to excel #########################
wb = Workbook()

sheet1 = wb.add_sheet("2022 Rushing Totals")
# maps the first sheet within the excel file and titles it with the preset name 2022 Rushing Totals 

sheet1.write(0,0, "Name")
sheet1.write(0,1, "Team")
sheet1.write(0,2, "Position")
sheet1.write(0,3,"Age")
sheet1.write(0,4, "Games Played")
sheet1.write(0,5, "Games Started")
sheet1.write(0,6, "Attempts")
sheet1.write(0,7, "Yards")
sheet1.write(0,8, "Touchdowns Scored")
sheet1.write(0,9, "First Downs Rushing")
sheet1.write(0,10,"Longest Rush Attempt")
sheet1.write(0,11,"Rushing Yards Per Attempt")
sheet1.write(0,12,"Rushing Yards Per Game")
sheet1.write(0,13,"Fumbles")




# within sheet1 of the excel file the collumns 1 through 5 are named as above 

for i in range(0,156):
    sheet1.write((i)//3+1,i%3, datafound[i])
    # for the string value in the range it is written within its corresponding column from the list values found in datafound until the determined limit of values is reached
# modulo takes remainder so it does i/3 the puts the remainder in that row 

for i in range(0,572):
    sheet1.write((i)//11+1,i%11+3, datafound1[i])
        # tell it where the data should go 
        # for the string value in the range it is written within its corresponding column from the list values found in datafound until the determined limit of values is reached
# # what is added is where the column of new data input begins
wb.save('xlwt_Rushing_Totals_Data1.xls')
# the file with the newly entered information is then saved within my local disk --> github --> intro to programming --> final project file path



#it is erroring because i do not have enoiugh values
# when an exception occurs there is a problem and no other code in the block occurs 
# i ran this code only going to from 0 to 1 and it printed the age of one player but when I runn it with more I think it attempts to verwrite excisting data causing it to stop working whic hI need to take a look at 