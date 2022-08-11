from ast import If
import imp


import os
from pickle import FALSE, TRUE
from selenium import webdriver
from time import sleep
from PIL import Image

import requests
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import Select

#　from simshow import simshow  #以 pip install simple-imshow 安裝模組

from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

# 預約所需資訊
bSuccess = False
sAccount = "B123009147"
sPassword = "refd5302"
sDate = "2022-08-16"
sTime="19"
sDate = input("預計預約日期 (ex.2022-08-16) :")
sTime = input("預計預約時間 (ex.19) :")
sAccount = input("帳號 :")
sPassword = input("密碼 :")

delay = 0.1 #unit s
url = 'https://nd01.xuanen.com.tw/MobileHome/MobileHome'  #網頁

from selenium import webdriver
driver = webdriver.Chrome('D:/chromedriver')
driver.get(url)
driver.maximize_window()

sleep(delay)  #加入等待

# 點選 場地預約
driver.find_element_by_xpath('//*[@id="MainShow"]/div/div/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div').click()
sleep(delay)  #加入等待

# 點選 羽球
driver.find_element_by_xpath('//*[@id="Div_PlaceTypeList"]/table/tbody/tr/td/table/tbody/tr/td[1]').click()
sleep(delay)  #加入等待

# 點選 同意
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(delay)  #加入等待

driver.find_element_by_xpath('//*[@id="But_agree"]').click()
sleep(delay)  #加入等待

# 登入
account = driver.find_element_by_xpath('//*[@id="txt_Account"]')
account.clear()
account.send_keys(sAccount)

passoord = driver.find_element_by_xpath('//*[@id="txt_Pass"]')
passoord.clear()
passoord.send_keys(sPassword)

driver.find_element_by_xpath('//*[@id="DivLogin"]/table/tbody/tr[3]/td/input').click()
sleep(delay)  #加入等待

# 選擇日期
select = Select(driver.find_element_by_xpath('//*[@id="DropDownList_SearchDate"]'))
select.select_by_value(sDate)
sleep(delay)  #加入等待

# 選擇時間
time_row = ( int(sTime) - 5)*2-1

for column in range(2, 8):
    xpath = '//*[@id="Div_PlaceBookingList"]/table/tbody/tr[3]/td/table/tbody/tr[%d]/td[%d]/img' %(time_row, column)
    imageTitle= driver.find_element_by_xpath(xpath).get_attribute("title")
    if (imageTitle == "可預約"):
        bSuccess = True
        driver.find_element_by_xpath(xpath).click()
        
        # 點選 確定預約
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(delay)  #加入等待
        driver.find_element_by_xpath('//*[@id="btn_PlaceBook"]').click()
        sleep(delay)  #加入等待
        print('預約完成！!!')
        break
    

sleep(1)  #加入等待

if(bSuccess == False):
    print('預約失敗 T_T')
    
os.system('pause')
        
