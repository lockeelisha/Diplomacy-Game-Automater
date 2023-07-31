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
import undetected_chromedriver as uc

# ask for types of games
prefix = input('What is the game server?\n')
type = input('What is the game type?')
basenumber = input("What game number are you starting from?")
game_total = input("How many games would you like?")

# initiate webdriver
# put this in parentheses if error happens ChromeDriverManager().install()
driver = uc.Chrome()


# Using Chrome to access web
# Open the website
driver.get('https://backstabbr.com')

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

elem = driver.switch_to.active_element

# Create new games
for i in range(int(game_total)):
    
    # Open new Chrome Tab
    driver.switch_to.new_window('tab')
    
    # Open Backstabbr
    driver.get('https://www.backstabbr.com/game/new')
    
    # Format Game number correctly
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
        driver.find_element(By.ID, "game_description").send_keys("For experienced and dedicated players. You must have 96% of your turns made and at least 10 games played, or you could be a part of the Olympus Diplomacy Community. https://discord.gg/TkYsTs6nJN")
    elif prefix == "Demosthenes" and type == "Gunboat":
        driver.find_element(By.ID, "game_description").send_keys("Demosthenes Gunboat Series. No press, fast adjudication, 24 hour game, 12 hr build/retreat. Welcome to the world of the orator! For more games, join here! https://discord.gg/4TvjxR3CuH")
    elif prefix == "Demosthenes" and type == "Press":
        driver.find_element(By.ID, "game_description").send_keys("Another game in the Demosthenes Series. Full press, fast adjudication, 24 hour game, 12 hr build/retreat. Welcome to the world of the orator! For more games, join here! https://discord.gg/4TvjxR3CuH")
    else:
        driver.find_element(By.ID, "game_description").send_keys("ERROR")
    
    driver.find_element(By.ID, "type_public").click()
    if type in ("Gunboat" , "Long Gunboat"):
        driver.find_element(By.ID, "press_never_allowed").click()
    else:
        driver.find_element(By.ID, "press_always_allowed").click()
    
    zone = Select(driver.find_element(By.ID, 'time_zone'))
    zone.select_by_value('US/Eastern')

    initial = Select(driver.find_element(By.ID, 'initial_adjudication_period'))
    initial.select_by_value('2880')

    springdaily = Select(driver.find_element(By.ID, 'orders_adjudication_period'))
    if type == "Long Gunboat":
        springdaily.select_by_value('4320')

    buildretreats = Select(driver.find_element(By.ID, 'build_and_retreat_adjudication_divisor'))
    if type == "Long Gunboat":
        buildretreats.select_by_value('1')
    
    driver.find_element(By.XPATH, "//input[@name='name']").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    """ for i in range(2):
        body = driver.find_element(By.CSS_SELECTOR,'body')
        body.send_keys(Keys.PAGE_DOWN) """

    elem = driver.switch_to.active_element

    if prefix == "Demosthenes":
        driver.find_element(By.ID, "skip").click()
        body = driver.find_element(By.CSS_SELECTOR,'body')
        body.send_keys(Keys.PAGE_DOWN)
        # elem = driver.switch_to.active_element
        driver.find_element(By.ID, "fast_adjudication").click()
    elif type in ("Gunboat" , "Long Gunboat"):
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
    else:
        driver.find_element(By.ID, "begin_when_full").click()
        driver.find_element(By.ID, "skip").click()
        body = driver.find_element(By.CSS_SELECTOR,'body')
        body.send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.ID, "grace_period").click()

input('Confirm that you have taken care of Discord channels\n')