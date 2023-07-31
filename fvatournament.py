# os for file management
import os
import undetected_chromedriver as uc

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# ask for types of games
prefix = input('What is the game prefix?\n')
# type = input('What is the game type?')
basenumber = input("What game number are you starting from?")
game_total = input("How many games would you like?")

# initiate webdriver
# put this in parentheses if error happens ChromeDriverManager().install()
driver = uc.Chrome()


# Using Chrome to access web
# Open the website
driver.get('https:/backstabbr.com')

try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "large_login"))
    )
except:
        driver.quit()

# Click sign-in
driver.find_element(By.ID, "large_login").click()

# Bypass Bot Verification
input('Confirm that you have logged in via Google\n')

# Create new games
for i in range(int(game_total)):
    for x in range(2):
        # Open new Chrome Tab
        driver.switch_to.new_window('tab')
        
        # Open Backstabbr
        driver.get('https://www.backstabbr.com/game/new')
        
        # Format Game number correctly
        currentgame = int(basenumber) + int(i)
        game = str(currentgame)
        game_number = str(x + 1)
        
        # Make sure it loaded
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "game_description"))
        )
        except:
            driver.quit()
        
        elem = driver.switch_to.active_element

        driver.find_element(By.XPATH, "//input[@name='name']").clear()
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(prefix + " "  + game + "-" + game_number)
        driver.find_element(By.ID, "game_description").send_keys("Part of the Olympus FvA Tournament. https://discord.gg/TkYsTs6nJN")
        
        # driver.find_element(By.ID, "type_public").click()
        driver.find_element(By.ID, "press_never_allowed").click()
            
        zone = Select(driver.find_element(By.ID, 'time_zone'))
        zone.select_by_value('US/Eastern')

        initial = Select(driver.find_element(By.ID, 'initial_adjudication_period'))
        initial.select_by_value('2880')

        retreats = Select(driver.find_element(By.ID, 'build_and_retreat_adjudication_divisor'))
        retreats.select_by_value('1')

        driver.find_element(By.XPATH, "//input[@name='name']").click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        driver.find_element(By.ID, "begin_when_full").click()
        driver.find_element(By.ID, "skip").click()
        elem = driver.switch_to.active_element
        body = driver.find_element(By.CSS_SELECTOR,'body')
        body.send_keys(Keys.PAGE_DOWN)
        try:
            element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "game_description"))
            )
        except:
            driver.quit()

        driver.find_element(By.ID, "fast_adjudication").click()
        driver.find_element(By.ID, "grace_period").click()


input('Confirm that you have taken care of Discord channels\n')