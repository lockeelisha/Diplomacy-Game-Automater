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
from selenium.webdriver.support.select import Select
import time


prefix = input('What is the game server?\n')
type = input('What is the game type?')
basenumber = input("What game number are you starting from?")
game_total = input("How many games would you like?")

driver = uc.Chrome(use_subprocess=True)

load_dotenv()
email = str(os.getenv('EMAIL'))
password  = str(os.getenv('PASSWORD'))


# Using Chrome to access web
# Open the website
driver.get('https:/backstabbr.com')

# Bypass Bot Verification
input('Confirm that you have logged in via Google\n')

original_window = driver.current_window_handle
print(driver.current_window_handle)



for i in range(int(game_total)):
    print(i)
    driver.switch_to.new_window('tab')
    driver.get('https://www.backstabbr.com/game/new')
    currentgame = int(basenumber) + int(i)
    game = str(currentgame)
    
    # Make sure it loaded
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "game_description"))
    )
    except:
        driver.quit()
    
    driver.find_element(By.XPATH, "//input[@name='name']").clear()
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(prefix + " " + type + " " + game)
    if prefix == "Olympus":
        driver.find_element(By.ID, "game_description").send_keys("For experienced and dedicated players. You must have 96% of your turns made and at least 10 games played, or you could be a part of the Olympus Diplomacy Community. https://discord.gg/9SymATUwwW")
    elif prefix == "Demosthenes" and type == "Gunboat":
        driver.find_element(By.ID, "game_description").send_keys("Demosthenes Gunboat Series. No press, fast adjudication, 24 hour game, 12 hr build/retreat. Welcome to the world of the orator! For more games, join here! https://discord.gg/4TvjxR3CuH")
    elif prefix == "Demosthenes" and type == "Press":
        driver.find_element(By.ID, "game_description").send_keys("Another game in the Demosthenes Series. Full press, fast adjudication, 24 hour game, 12 hr build/retreat. Welcome to the world of the orator! For more games, join here! https://discord.gg/4TvjxR3CuH")
    else:
        driver.find_element(By.ID, "game_description").send_keys("ERROR")
    
    driver.find_element(By.ID, "type_public").click()
    if type == "Gunboat":
        driver.find_element(By.ID, "press_never_allowed").click()
    else:
        driver.find_element(By.ID, "press_always_allowed").click()
    
    zone = Select(driver.find_element(By.ID, 'time_zone'))
    zone.select_by_value('US/Eastern')

    initial = Select(driver.find_element(By.ID, 'initial_adjudication_period'))
    initial.select_by_value('2880')

    
    

    driver.find_element(By.XPATH, "//input[@name='name']").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


    if prefix == "Demosthenes":
        driver.find_element(By.ID, "skip").click()
        body = driver.find_element(By.CSS_SELECTOR,'body')
        body.send_keys(Keys.PAGE_DOWN)
        elem = driver.switch_to.active_element
        driver.find_element(By.ID, "fast_adjudication").click()
    elif type == "Gunboat":
        driver.find_element(By.ID, "begin_when_full").click()
        driver.find_element(By.ID, "skip").click()
        elem = driver.switch_to.active_element
        body = driver.find_element(By.CSS_SELECTOR,'body')
        body.send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.ID, "fast_adjudication").click()
    else:
        driver.find_element(By.ID, "begin_when_full").click()
        driver.find_element(By.ID, "skip").click()

input('Confirm that you have taken care of Discord channels\n')