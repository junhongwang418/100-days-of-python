from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os

load_dotenv()

FACEBOOK_USERNAME = os.getenv('FACEBOOK_USERNAME')
FACEBOOK_PASSWORD = os.getenv('FACEBOOK_PASSWORD')

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.instagram.com/')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button').click()
time.sleep(2)

driver.find_element_by_name('email').send_keys(FACEBOOK_USERNAME)
driver.find_element_by_name('pass').send_keys(FACEBOOK_PASSWORD)
driver.find_element_by_id('loginbutton').click()
time.sleep(10)

driver.get('https://www.instagram.com/chefsteps/')
time.sleep(2)

driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(5)

follow_buttons = driver.find_elements_by_css_selector('ul div li div button')

for button in follow_buttons:
    button.click()
    time.sleep(1)

driver.quit()
