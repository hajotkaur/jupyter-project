from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import csv


#initialize the chrome web driver
driver = webdriver.chrome()

page_url = 'https://ww150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401'


#fetching  the web page 
driver.get(page_url)


# Wair for the table to load
driver.implicity_wait(10)

# Get the page source after javaScript execution 
page_source = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find the table element 
table = soup.find(id='simpleTable')

if table:
    #Extract column headers
    headers = []




