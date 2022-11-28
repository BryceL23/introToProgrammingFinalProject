# Overview 
    # Fantasy Football Data Snatcher, allows for a faster and more efficient way to take data from fantasy football websites to excel files to later be analysed. 

    # During my statistics class earlier this school year we were tasked with a project to create graphs and analyze data on a topic of our choice. During the time when this project was introduced I was still workign on that project and was unable to find a single website that would have all the data poitns I was looking for and as a result had to gather data from multiple sites into a single excel file and format it correctly so I was usable. I wanted to create a solution for this problem and would like to create a sceen scraper to bring the new data after each week to the excel spreadsheet ready to be turned into graphs so trends for players and teams can be analyzed.

# Sources:
    # look at automatetheboringstuff.com
    # https://realpython.com/python-web-scraping-practical-introduction/#build-your-first-web-scraper
# Libraries:

# Steps of Construction:
    # Find the website I wish to draw data from
    # read articles and learn how to build a screen scrapper
    # write the code that will allow me to record the data from the website and into a file which could be used in a later use in an excel file
    # make a path to send the code to an excel or google sheet 

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Bryce.Linton23/Downloads/chromedriver_win32 (1).zip')
# where we imput the url we are using below 
driver.get()
results = []
content = driver.page_source
soup = BeautifulSoup(content)


for element in soup.findAll(attrs='d3-l-grid--outer d3-l-section-row'):
    name = element.find('h1')

