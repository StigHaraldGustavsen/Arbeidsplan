import time
import random
import os

from dotenv import load_dotenv
load_dotenv()

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome  import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

user_name = os.environ['UN']
password = os.environ['PW']

driver.get("https://Arbeidsplan.uloba.no/Home/PersonIndexPrint")

user_name_field = driver.find_element(By.ID,value="login-username")
user_name_field.send_keys(user_name)
next_button = driver.find_element(By.ID,value='btn-next')
next_button.click()

time.sleep(1+random.randint(0,2))

password_field = driver.find_element(By.ID,value="login-password")
password_field.send_keys(password)
login_button = driver.find_element(By.ID,value='btn-login')
login_button.click()

time.sleep(1+random.randint(0,2))

driver.get('https://arbeidsplan.uloba.no/Home/PersonIndexPrint')

#page = driver.page_source
#tablesection = page.split('</form></div>')[1]
#tablesection = page.split('<div class="page-break"></div>')[0]

print(driver.page_source)
driver.quit()