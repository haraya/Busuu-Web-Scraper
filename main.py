# Import libraries
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Create Selenium Chrome browser instance
def create_driver():
    options = Options() # creates a configuration object for chrome
    options.add_experimental_option("detach", True) # Keep the browser window open after script finishes
    driver = webdriver.Chrome(options=options) # Starts a new Chrome browser with options configutation
    return driver
