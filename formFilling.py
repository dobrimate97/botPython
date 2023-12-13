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
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)   
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    

browser.get("https://adidas.de")
time.sleep(5) #WAIT FOR SELECTOR?

browser.find_element(By.XPATH,"//span[text()='I accept functional and marketing cookies etc.']").click()
#browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
#time.sleep(2)
#browser.execute_script("window.scrollTo(0,-document.documentElement.scrollHeight)")
#browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
#time.sleep(2)
#browser.execute_script("window.scrollTo(0,-document.documentElement.scrollHeight)")
#time.sleep(5)

browser.find_element(By.LINK_TEXT, 'werde mitglied').click()
time.sleep(3)

email = browser.find_element(By.ID, "email")
email.send_keys(account_data[2])
browser.find_element(By.XPATH,"//span[text()='WEITER']").click()

time.sleep(200)