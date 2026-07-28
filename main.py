# Import libraries
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Function for creating Selenium Chrome browser instance
def create_driver():
    options = Options() # creates a configuration object for chrome
    options.add_experimental_option("detach", True) # Keep the browser window open after script finishes
    driver = webdriver.Chrome(options=options) # Starts a new Chrome browser with options configutation
    return driver

# Function for Scroll 
def scrolling_load_content(driver, pause=1.2, max_times = 30): 
    """
    This function scroll the browser for content and wait a bit and try a few times if needed.

    Args:
        driver (object): It represents the browser session created by Selenium.
        pause (float): It is the amount of time the function waits between each scroll step.
        max_times(int): It is the maximum number of times the loop will run.
    """

    scroll_height = driver.execute_script("return document.body.scrollHeight") # It is about to know how tall is whole page.
    times = 0
    while times < max_times:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Run JS inside the browser and go down to the full height of the page
        time.sleep(pause)
        new_height = driver.execute_script("return document.body.scrollHeight") # Measure the page height again after the scroll
        if new_height == scroll_height:
            times += 1
        else:
            times = 0
            scroll_height = new_height

# Function for extracting chapters and lessons
def extract_chapters_lessons(driver):
    """
    Run this JS script in the DOM and return a list of nodes called chapter.
    """
    script = """
    const nodes = document.querySelectorAll('h3, [data-testid="lesson_card"]');
    const result = [];
    nodos.forEach(n => {
        if (n.tagName.toLowerCase() === 'h3') {
            result.push({tipo: 'chapter', text: n.textContent.trim()});
        } else {
            const title = n.querySelector('[data-testid="dialog_level_title"]');
            const subtitle = title ? title.nextElementSibling : null;
            result.push({
                tipy: 'lesson',
                title: title ? title.textContent.trim() : null,
                subtitle: subtitle ? subtitle.textContent.trim() : null
            });
        }
    });
    return result;
    """
    return driver.execute_script(script)
