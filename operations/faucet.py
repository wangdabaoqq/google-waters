'''
Author: baobaobao
Date: 2025-03-03 16:07:04
LastEditTime: 2025-03-03 22:30:39
LastEditors: baobaobao
'''
from DrissionPage import Chromium
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

def faucet(tab: Chromium):
  tab.get('https://cloud.google.com/application/web3/faucet/ethereum/sepolia')
  select = tab.ele('xpath://*[@class="cw3-space-above-base"]//cw3-faucet-drip-form//form//mat-form-field').child()
  select.click()
  tab.ele('#mat-option-1').click()
  address = os.getenv('ADDRESS')
  tab.ele('#mat-input-0').input(address)
  tab.ele('xpath://section[@class="cw3-space-above-base"]//form/button').click()
  sleep(10)
  get_title = tab.ele('.mat-mdc-card-title')
  if get_title:
    print('领取成功')
  else:
    get_body = tab.ele('xpath://*[@class="xap-callout-content"]//xap-callout-body')
    print(get_body.text)
    print('领取失败')
