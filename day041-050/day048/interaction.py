from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://en.wikipedia.org/wiki/Main_Page')
num_articles_tag = driver.find_element_by_css_selector("div#articlecount a")
print(num_articles_tag.text)

driver.quit()
