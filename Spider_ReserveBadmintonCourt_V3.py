#!/usr/bin/env python
# coding: utf-8
import os
import requests, re
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

areaList = {
  'A': '83',
  'B': '84',
  'C': '1074',
  'D': '1075',
  'E': '87',
  'F': '2225',
}

def Crawling():
    headers = {
      'authority': 'nd01.xuanen.com.tw',
      'accept': '*/*',
      'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
      'origin': 'https://nd01.xuanen.com.tw',
      'referer': 'https://nd01.xuanen.com.tw/BPMember/BPMemberLogin',
      'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest'
    }


    session = requests.Session()
    payload = {
      'tFlag': '0',
      'account': 'B123009147',
      'pass': 'refd5302'
    }

    session.post("https://nd01.xuanen.com.tw/BPMember/BPMemberLogin", headers=headers, data=payload)

    url = "https://nd01.xuanen.com.tw/BPLocationBooking/BPLocationBooking?tFlag=3"


    # 建立日期與時間的物件
    current_dateTime  = datetime.now()
    day_origin = current_dateTime.day
    bIsWait = True

    # 等待時間00:00開始預約場地
    while(bIsWait):
        current_dateTime  = datetime.now()
        current_time = current_dateTime.strftime("%H:%M:%S")
        current_day = current_dateTime.day
        if(current_time >= '00:00:00' and current_day > day_origin):
            bIsWait = False

    headers = {
      'authority': 'nd01.xuanen.com.tw',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
      'cache-control': 'max-age=0',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://nd01.xuanen.com.tw',
      'referer': 'https://nd01.xuanen.com.tw/BPLocationBooking/BPLocationBooking?tFlag=2',
      'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    firstTime = '19'
    secondTime = '20'

    nextWeek = datetime.today() + timedelta(days=7)
    date = nextWeek.strftime('%Y-%m-%d')

    isFirstSuccess = 0
    isSecondSuccess = 0

    for key in areaList:
      print(key + '場')
      if not isFirstSuccess:
        firstRes = session.post(url, headers=headers, data='LC=1&id='+ areaList[key] +'&date='+ date +'&time='+ firstTime)
        isFirstSuccess = re.search("^.*成功.*$", bs(firstRes.text, 'html.parser').select('div.box3')[0].text)
        print(isFirstSuccess)
      if not isSecondSuccess:
        secondRes = session.post(url, headers=headers, data='LC=1&id='+ areaList[key] +'&date='+ date +'&time='+ secondTime)
        isSecondSuccess = re.search("^.*成功.*$", bs(secondRes.text, 'html.parser').select('div.box3')[0].text)
        print(isSecondSuccess)

Crawling()

os.system('pause')