from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://secure-sit.fidelity.com.tw/")
print(driver.title)
driver.close()
driver.quit()
