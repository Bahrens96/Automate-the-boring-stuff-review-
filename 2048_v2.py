# 2048 tutorial 
# From Al Sweigart's Automate the boring stuff chapter 12
# https://automatetheboringstuff.com/2e/chapter12/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

PATH = "C:\Program Files (x86)\chromedriver.exe" # where the driver is on the computer 
driver = webdriver.Chrome(PATH)

driver.get('https://play2048.co/')

directions = [Keys.UP, Keys.DOWN, Keys.RIGHT, Keys.LEFT]

driver.set_page_load_timeout(30)	# wait  30 secs for page to load

i= 1
for i in range(100): #loop 100 times (enough) to play the game 
	i+=1 #incriment the loop
	for direction in directions: 
		choice = random.choice(direction) # select a direction at random
		#print_current_tiles(i)
		ActionChains(driver).send_keys(choice).perform() #press a random key 