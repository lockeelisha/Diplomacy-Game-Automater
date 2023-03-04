# os for file management
import os
import selenium
import undetected_chromedriver as uc


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys


driver = uc.Chrome(use_subprocess=True)

load_dotenv()
email = str(os.getenv('EMAIL'))
password  = str(os.getenv('PASSWORD'))


# Using Chrome to access web
# Open the website
driver.get('https://accounts.google.com/ServiceLogin')

sec = input('Confirm that you have logged in via Google\n')


new_finder = "//input[@type='email']"
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, new_finder)))
except:
    print("Page title is : " + driver.title)
    print("I QUIT")

driver.find_element(By.XPATH, new_finder).send_keys(email + Keys.ENTER)

finder = "next"
# LgbsSe
try:
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, finder)))
except:
    print("I QUIT HERE")

driver.find_element(By.ID, finder).click()

