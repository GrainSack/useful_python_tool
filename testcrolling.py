from random import sample
from tkinter import TRUE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

browser = webdriver.Chrome('C:/chromedriver.exe')

browser.get('https://www.naver.com')
browser.implicitly_wait(10)

browser.find_element_by_css_selector('a.nav.shop').click()

time.sleep(2)

search = browser.find_element_by_css_selector('input.co_srh_input._input')

search.click()

search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

#스크롤 전 높이
before_h = browser.execute_script('return window.scrollY')

#scroll

while True:
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    #스크롤 사이 페이지 로딩시간
    time.sleep(1)
    
    #스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    
    if after_h == before_h:
        break
    before_h = after_h

#csv 생성
f = open(r"C:\Users\Kss\Desktop\Graduate\Deeplearning\crolling/data.csv", 'w', encoding= 'CP949', newline='')
csvWriter = csv.writer(f)
#상품정보
items = browser.find_elements_by_css_selector('.basicList_info_area__17Xyo')

for item in items:
    name = item.find_element_by_css_selector('.basicList_title__3P9Q7').text
    try:
        price = item.find_element_by_css_selector('.price_num__2WUXn').text
    except:
        price = '판매중단'
    link = item.find_element_by_css_selector('.basicList_title__3P9Q7 > a').get_attribute('href')
    print(name, price, link)
    #데이터 쓰기
    csvWriter.writerow([name, price, link])
    
#파일 닫기
f.close()