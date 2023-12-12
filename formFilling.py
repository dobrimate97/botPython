from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://adidas.de")
#browser.get("https://www.opera.com/download")
time.sleep(5)
#cookies = browser.find_element(By.LINK_TEXT, 'Accept cookies').click()
#cookies = browser.find_element(By.XPATH, "//span[contains(text(),'I ACCEPT FUNCTIONAL AND MARKETING COOKIES ETC.')]").click()
#browser.find_element(By.LINK_TEXT, 'werde mitglied').click()
browser.find_element(By.XPATH,"//span[text()='I accept functional and marketing cookies etc.']").click()
time.sleep(3)
