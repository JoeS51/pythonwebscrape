from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd

wait = WebDriverWait(webdriver, 20)

driver = webdriver.Chrome()

driver.get("https://www.chelseafc.com/en/teams/profile/cole-palmer")

title = driver.title

driver.implicitly_wait(0.5)

goals_scored = driver.find_elements(By.CLASS_NAME, value="player-stat__title")

print(len(goals_scored))

i = 0
for goal in goals_scored:
    
    print("index" + str(i))
    print(goal.text)
    i+=1


#print("GOALS: " + str(goals_scored))

print(title)

driver.quit()