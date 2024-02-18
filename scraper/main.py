#!/usr/bin/env python
import time
import random
import os
import sys
from datetime import datetime

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

new_directory = "/app"
os.chdir(new_directory)

updated_directory = os.getcwd()
print("Updated Working Directory:", updated_directory)

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print('no .env file, using external enviromental variable')

#from bs4 import BeautifulSoup
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

user_name = os.environ['ULOBA_USERNAME']
password = os.environ['ULOBA_PASSWORD']

if len(user_name) == 0 or len(password) == 0:
    print('no username or password, add them to enviromentla variables: ULOBA_USERNAME, ULOBA_PASSWORD')
    sys.exit()

print('logging in with: '+user_name+" and pw:"+len(password)*'*')

driver.get("https://Arbeidsplan.uloba.no/Home/PersonIndexPrint")

time.sleep(1)

user_name_field = driver.find_element(By.ID,value="login-username")
user_name_field.send_keys(user_name)
next_button = driver.find_element(By.ID,value='btn-next')
next_button.click()

time.sleep(1+random.randint(0,1))

password_field = driver.find_element(By.ID,value="login-password")
password_field.send_keys(password)
login_button = driver.find_element(By.ID,value='btn-login')
login_button.click()

time.sleep(1+random.randint(0,1))

driver.get('https://arbeidsplan.uloba.no/Home/PersonIndexPrint')


#print(driver.page_source)

page = driver.page_source
try:
    page = page.split('</form></div>')[1]
    page = page.split('<div class="page-break"></div>')[0]
    page = "<p>Extracted:"+str(datetime.now())+"</p>/n"+page
    f = open("tables.html", "w")
    f.write(page)
    f.close()
except:
    print(str(datetime.now)+" Failed to find properly formatted data") 

driver.quit()

print("---------- finnished ------------ "+str(datetime.now()))


