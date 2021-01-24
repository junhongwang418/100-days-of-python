from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL_ADDRESS = os.getenv('MY_EMAIL_ADDRESS')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=103644278&keywords=software%20engineer&location=United%20States')

time.sleep(1)

driver.find_element_by_link_text('Sign in').click()

time.sleep(1)

driver.find_element_by_name('session_key').send_keys(MY_EMAIL_ADDRESS)
driver.find_element_by_name('session_password').send_keys(LINKEDIN_PASSWORD)
driver.find_element_by_css_selector('form button').click()

time.sleep(1)

driver.find_element_by_xpath(
    '/html/body/div[7]/div[3]/div[3]/div/div/section[1]/div/div/section[2]/div/ul/li[2]/button').click()
time.sleep(2)

jobs = driver.find_elements_by_css_selector(
    'div.jobs-search-results ul li div div div div div a.disabled')

for job in jobs:
    job.click()

    time.sleep(1)

    try:
        driver.find_element_by_css_selector(
            'div.jobs-apply-button--top-card button').click()
        time.sleep(1)
        button = driver.find_element_by_css_selector('form footer button')
        if button.text == 'Submit application':
            button.click()
            time.sleep(1)
            driver.find_element_by_css_selector(
                'div#artdeco-modal-outlet div div button').click()
            time.sleep(1)
        else:
            driver.find_element_by_css_selector(
                'div#artdeco-modal-outlet div div button').click()
            time.sleep(1)
            driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/div[3]/button[2]').click()
            time.sleep(1)
    except:
        print('error')


driver.quit()
