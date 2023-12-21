import requests
from bs4 import BeautifulSoup
import gspread
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver
import time
from datetime import datetime
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

li = []

for j in range(0, 10):
    url = 'https://www.glassdoor.co.in/Reviews/index.htm?overall_rating_low=3.5&page='+str(j+1)+'&filterType=RATING_OVERALL'
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for c in soup.find('div', class_='col-md-12 col-lg-8').find_all('div', class_='mt-0 mb-std p-std css-mdw3bo css-errlgf'):
        try:
            icon_link = c.find('img', {"data-test": "employer-logo"})['src']
        except:
            icon_link = 'No Info'
        try:
            name = c.find('h2', {"data-test": "employer-short-name"}).text.strip()
        except:
            name = 'No Info'
        try:
            rating = c.find('span',{"data-test": "rating"}).text.strip()
        except:
            rating = "No Info"
        try:
            reviews = c.find('h3', {"data-test": "cell-Reviews-count"}).text.strip()
        except:
            reviews = 'No Info'
        try:
            salary = c.find('h3', {"data-test":"cell-Salaries-count"}).text.strip()
        except:
            salary = 'No Info'
        try:
            jobs = c.find('h3', {"data-test":"cell-Jobs-count"}).text.strip()
        except:
           jobs = 'No Info'
        try:
            location = c.find('span', {"data-test":"employer-location"}).text.strip()
        except:
            location = 'No Info'
        try:
            size = c.find('span', {"data-test":"employer-size"}).text.strip()
        except:
            size = 'No Info'
        try:
            industry = c.find('span', {"data-test":"employer-industry"}).text.strip()
        except:
            industry = 'No Info'
        try:
            description = c.find('p', class_='css-1sj9xzx css-56kyx5').text.strip()
        except:
            description = 'No Info'

        dictt = {
            'Icon': icon_link,
            'Company': name,
            'Ratings': rating,
            'Reviews': reviews,
            'Salaries': salary,
            'Jobs': jobs,
            'Location': location,
            'Company Size': size,
            'Industry': industry,
            'Description': description
        }
        li.append(dictt)

df = pd.DataFrame(li)
df.to_csv('glassdoor_data.csv')