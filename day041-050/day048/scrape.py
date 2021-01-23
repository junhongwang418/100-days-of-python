from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.python.org/')
events = driver.find_elements_by_css_selector("div.shrubbery ul.menu li")
print([event.text for event in events])

driver.quit()
