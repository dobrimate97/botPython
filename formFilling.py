from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from accountManaging import account_data
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://adidas.de")
time.sleep(5)

browser.find_element(By.XPATH,"//span[text()='I accept functional and marketing cookies etc.']").click()
browser.find_element(By.LINK_TEXT, 'werde mitglied').click()
time.sleep(3)

email = browser.find_element(By.ID, "email")
email.send_keys(account_data[0])
time.sleep(10)