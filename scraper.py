
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep # insert pauses in code
import pandas as pd

# Writing a function to scrape the data. It will receive
# List of currency codes
# Start & end date
# Boolean for exporting data as .csv

def get_currencies(currencies, start, end, export_csv=False):
    frames = []
    for currency in currencies:
    my_url = f'https://br.investing.com/currencies/usd-{currency.lower()}-historical-data'
    option = Options()
    option.headless = False
    driver = webdriver.Chrome(options=option)
    driver.get(my_url)
    driver.maximize_window()




# Tutorial from https://www.freecodecamp.org/news/how-to-code-a-scraping-bot-with-selenium-and-python/