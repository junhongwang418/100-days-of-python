from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os

load_dotenv()

TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(5)
        self.driver.find_element_by_link_text('GO').click()

        time.sleep(60)

        self.down = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')

        time.sleep(5)

        self.driver.find_element_by_name(
            'session[username_or_email]').send_keys(TWITTER_USERNAME)

        self.driver.find_element_by_name(
            'session[password]').send_keys(TWITTER_PASSWORD)

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()

        time.sleep(5)

        content = 'Day 51 of #100DaysOfCode: Built a program that tweets this tweet using @SeleniumHQ.\n\n@LondonAppBrewer #Python\n'

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').send_keys(content)

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]').click()

        self.driver.quit()
