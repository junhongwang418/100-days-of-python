from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os

load_dotenv()

FACEBOOK_USERNAME = os.getenv('FACEBOOK_USERNAME')
FACEBOOK_PASSWORD = os.getenv('FACEBOOK_PASSWORD')

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://tinder.com/')
time.sleep(2)

driver.find_element_by_xpath(
    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()
time.sleep(2)

driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_name('email').send_keys(FACEBOOK_USERNAME)
driver.find_element_by_name('pass').send_keys(FACEBOOK_PASSWORD)
driver.find_element_by_name('login').click()

driver.switch_to.window(driver.window_handles[0])

time.sleep(2)

driver.find_element_by_xpath(
    '//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

time.sleep(2)

driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()

time.sleep(2)

driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()

time.sleep(2)

for _ in range(5):
    driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button').click()
    time.sleep(2)

driver.quit()
