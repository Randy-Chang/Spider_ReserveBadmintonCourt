import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from datetime import datetime

#　from simshow import simshow  #以 pip install simple-imshow 安裝模組
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())

# 預約所需資訊
bSuccess = False
sAccount = "B123009147"
sPassword = "refd5302"
sDate = "2022-08-16"
sTime="19"
#sDate = input("預計預約日期 (ex.2022-08-16) :")
#sTime = input("預計預約時間 (ex.19) :")
#sAccount = input("帳號 :")
#sPassword = input("密碼 :")
bIsWait = True
delay1 = 0.1 #unit s
delay2 = 0.05 #unit s
url = 'https://nd01.xuanen.com.tw/MobileHome/MobileHome'  #網頁

driver = webdriver.Chrome('D:/chromedriver')

# 建立日期與時間的物件
current_dateTime  = datetime.now()
day_origin = current_dateTime.day


# 改變瀏覽器的縮放為150%
driver.get('chrome://settings/')
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(1.5);')

# 瀏覽器網址連線至目標網站
driver.get(url)

# 瀏覽器放大
#driver.maximize_window() 

sleep(delay1)  #加入等待

# 點選 場地預約
driver.find_element("xpath", '//*[@id="location_text"]').click()
sleep(delay1)  #加入等待

# 點選 羽球
driver.find_element("xpath", '//*[@id="chooselist3"]/div/div/div/div[1]').click()
sleep(delay1)  #加入等待

# 等待時間23:59開始預約場地
# while(bIsWait):
    # current_dateTime  = datetime.now()
    # current_time = current_dateTime.strftime("%H:%M:%S")
    # urrent_day = current_dateTime.day
    # if(current_time >= '23:59:00'):
    #     bIsWait = False

# 填入帳號
account = driver.find_element("xpath",'//*[@id="txt_Account"]')
account.clear()
account.send_keys(sAccount)


# 填入密碼
passoord = driver.find_element("xpath",'//*[@id="txt_Pass"]')
passoord.clear()
passoord.send_keys(sPassword)

# 捲動視窗到底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 

# 點選  登入
driver.find_element("xpath", '//*[@id="subform_Login"]/div/div/div[3]').click()
sleep(delay1)  #加入等待

# 點選 同意閱讀
driver.find_element("xpath", '//*[@id="label1"]').click()

# 等待時間00:00開始預約場地
# while(bIsWait):
#     current_dateTime  = datetime.now()
#     current_time = current_dateTime.strftime("%H:%M:%S")
#     current_day = current_dateTime.day
#     if(current_time >= '00:00:00' and current_day > day_origin):
#         bIsWait = False
        
# 點選 預約場地
driver.find_element("xpath", '//*[@id="MainBlock"]/div[3]/div/div[3]/div[5]/div[2]').click()
sleep(delay2)  #加入等待

# 點選 最新日期
driver.find_element("xpath", '//*[@id="Div_List"]/table/tbody/tr/td/div[4]/div[1]').click()
sleep(delay2)  #加入等待

# 點選 晚上
driver.find_element("xpath", '//*[@id="Div_List"]/table/tbody/tr/td/div[1]/div[3]').click()
sleep(delay2)  #加入等待

for i in range(7, 19):
    xpath = '//*[@id="Div_List"]/table/tbody/tr/td/div[5]/div[%d]/div[2]/div' %(i)
    button = driver.find_element("xpath", xpath)
    if(button.text == '預約場地'):
        driver.find_element("xpath", xpath).click()
        driver.find_element("xpath", '//*[@id="subform_List"]/div[2]/div[2]/div[2]/div[1]').click()
        print('預約成功')
        break
        
driver.close()


os.system('pause')


#############################################################################################
# driver.find_element_by_xpath('').click()
# sleep(delay)  #加入等待



# 選擇日期
# select = Select(driver.find_element_by_xpath('//*[@id="DropDownList_SearchDate"]'))
# select.select_by_value(sDate)
# sleep(delay)  #加入等待

# 選擇時間
# time_row = ( int(sTime) - 5)*2-1

# for column in range(2, 8):
#     xpath = '//*[@id="Div_PlaceBookingList"]/table/tbody/tr[3]/td/table/tbody/tr[%d]/td[%d]/img' %(time_row, column)
#     imageTitle= driver.find_element_by_xpath(xpath).get_attribute("title")
#     if (imageTitle == "可預約"):
#         bSuccess = True
#         driver.find_element_by_xpath(xpath).click()
        
#         # 點選 確定預約
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         sleep(delay)  #加入等待
#         driver.find_element_by_xpath('//*[@id="btn_PlaceBook"]').click()
#         sleep(delay)  #加入等待
#         print('預約完成！!!')
#         break
    

# sleep(1)  #加入等待

# if(bSuccess == False):
#     print('預約失敗 T_T')
    
# os.system('pause')
        
