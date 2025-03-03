'''
Author: baobaobao
Date: 2025-03-03 13:16:30
LastEditTime: 2025-03-03 20:55:22
LastEditors: baobaobao
'''
from DrissionPage import Chromium
from time import sleep
from dotenv import load_dotenv
import os 

load_dotenv()

def login_google(tab):
  print('开始登录')
  tab.get('https://accounts.google.com/signin')
  if ('https://myaccount.google.com' in tab.url):
    return
  # email = tab.ele('.Xb9hP input[name="identifier"]')
  email = tab.ele('xpath://*[@class="Xb9hP"]/input[@name="identifier"]')
  get_email = os.getenv('EMAIL_ADDRESS')
  get_password = os.getenv('EMAIL_PASSWORD')
  # path://*[@id="identifierNext"]
  email.input(get_email)

  button = tab.ele('xpath://*[@id="identifierNext"]//button')
  button.click()

  password = tab.ele('xpath://*[@class="Xb9hP"]/input[@name="Passwd"]')
  password.input(get_password)

  button = tab.ele('xpath://*[@id="passwordNext"]//button')
  button.click()
