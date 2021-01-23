from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import threading
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://orteil.dashnet.org/cookieclicker/')
cookie = driver.find_element_by_id("bigCookie")

time.sleep(5)

driver.find_element_by_link_text('Got it!').click()

done = False


def tick():
    global done
    if done:
        return

    try:
        upgrade_tag = driver.find_element_by_css_selector(
            "div#upgrades div.enabled")
    except NoSuchElementException:
        product_tags = driver.find_elements_by_css_selector(
            "div#products div.enabled")
        if len(product_tags) > 0:
            product_tags[-1].click()
    else:
        upgrade_tag.click()
    finally:
        threading.Timer(10, tick).start()


def finish():
    global done
    print(driver.find_element_by_css_selector('div#cookies div').text)
    done = True


tick()

threading.Timer(300, finish).start()

while not done:
    cookie.click()

driver.quit()
