from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from accountManaging import account_data
import time
# TODO: FUNCKIÓKBA RENDEZNI MINDENT 
options = Options()
options.add_experimental_option("excludeSwitches",["enable-automation"])

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get("https://adidas.de")
time.sleep(5)

browser.find_element(By.XPATH,"//span[text()='I accept functional and marketing cookies etc.']").click()
browser.find_element(By.LINK_TEXT, 'werde mitglied').click()
time.sleep(3)

email = browser.find_element(By.ID, "email")
email.send_keys(account_data[2])
browser.find_element(By.XPATH,"//span[text()='WEITER']").click()

time.sleep(20)