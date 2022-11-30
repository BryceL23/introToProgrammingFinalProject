# Overview 
    # Fantasy Football Data Snatcher, allows for a faster and more efficient way to take data from fantasy football websites to excel files to later be analysed. 

    # During my statistics class earlier this school year we were tasked with a project to create graphs and analyze data on a topic of our choice. During the time when this project was introduced I was still workign on that project and was unable to find a single website that would have all the data poitns I was looking for and as a result had to gather data from multiple sites into a single excel file and format it correctly so I was usable. I wanted to create a solution for this problem and would like to create a sceen scraper to bring the new data after each week to the excel spreadsheet ready to be turned into graphs so trends for players and teams can be analyzed.

# Sources:
    # look at automatetheboringstuff.com
    # https://realpython.com/python-web-scraping-practical-introduction/#build-your-first-web-scraper
    # https://www.youtube.com/watch?v=mDveiNIpqyw
    # https://oxylabs.io/blog/python-web-scraping
# Libraries:

# Steps of Construction:
    # Find the website I wish to draw data from
    # read articles and learn how to build a screen scrapper
    # write the code that will allow me to record the data from the website and into a file which could be used in a later use in an excel file
    # make a path to send the code to an excel or google sheet 

# importing the installed libraries
import pandas as pd
# it is a library written for data manipulation and analytics 
from bs4 import BeautifulSoup
# a powerful library that allows users to pull data from HTML files to nagivate and search through data before 
from selenium import webdriver
# it is used to automate test cases which test the functionality of the actions to make sure the expected resulf occurs

driver = webdriver.Chrome(executable_path='C:/Users/Bryce.Linton23/OneDrive - Bellarmine College Preparatory/Intro_Computer_Programing/Final_Project_Excel_Files_Fantasy_Football')
# driver is the first variable we are suing which will state what our browser is and its location
# because Chrome is installed on our computer or engine we will be using that as our browser
# need to download the web driver version that matches our browser
driver.get('https://www.nfl.com/stats/player-stats/category/rushing/2022/reg/all/rushingyards/desc')
# this is the url that we will be gathering our data from 

results = []
# creating an empty list where the results from our screen scrape will be located 
content = driver.page_source
# creating the variable 'content' will store the page source derived from the url that we are getting our 
soup = BeautifulSoup(content)
# creating new variable soup that creates a parser which provides structure to a string value, it cannot grab the data from the HTML but it can 
driver.quit()
# this will force the browser to close

for element in soup.findAll(attrs='d3-l-grid--outer d3-l-section-row'):
    # it will iterate (repeatedy execute the code) through all the data that meets certain parameters 
    name = element.find('h1')
    # tells our code which data on the web page it needs to find 
    if name not in results:
        # will avoid adding duplicates to the list if the result is not present
        results.append(name.text)
        # will add the data stored in the variable name to the end of the list result and only the text found in the class 
df = pd.DataFrame({'stats' : results})
# creates a variable that will create a table, create and dictionary and collumn names within the parenthasis 
df.to_csv('stats.csv', index=False, encoding='utf-8')
# export the new table 