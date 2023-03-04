# os for file management
import os
import selenium


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

load_dotenv()
email = str(os.getenv('EMAIL'))
password  = str(os.getenv('PASSWORD'))


# Using Chrome to access web
# Open the website
driver.get('https:/backstabbr.com')
# Login
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "large_login"))
    )
except:
    driver.quit()

backstabbr_login_button = driver.find_element(By.ID, "large_login")
backstabbr_login_button.click()
print("Test 1")

finder = "//button[@data-provider-id='google.com']"

try:
    element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, finder)))
except:
    driver.quit()
    print("I QUIT HERE")

print("Test 2")

google_login_button = driver.find_element(By.XPATH, finder)
google_login_button.click()

finder_id = "PONK"
try:
    element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.ID, finder_id)))
except:
    driver.quit()
    print("I QUIT")