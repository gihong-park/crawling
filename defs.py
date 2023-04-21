from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

# 페이지에서 내용 가져오는 코드
def source(num):
    co = Options()
    co.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    chrome_driver= "C:/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, options=co)

    # 영수증 클릭
    p_click = driver.find_element_by_xpath(f'//*[@id="searchForm"]/div[2]/table[1]/tbody/tr[{num}]/td[8]/a').click()
    # 창 바꾸기
    driver.switch_to.window(driver.window_handles[-1])
    # 시간 늦추기
    time.sleep(0.7)
    # 창 정보 가져오기
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')
    # 이름
    name = driver.find_element_by_xpath('//*[@id="slipform"]/div/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td').text
    # 가격
    price100000 = driver.find_element_by_xpath('//*[@id="slipform"]/div/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[3]/table/tbody/tr[13]/td[9]').text.strip()
    price10000 = driver.find_element_by_xpath('//*[@id="slipform"]/div/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[3]/table/tbody/tr[13]/td[11]').text.strip()
    price1000 = driver.find_element_by_xpath('//*[@id="slipform"]/div/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[3]/table/tbody/tr[13]/td[13]').text.strip()
    price = price100000 + price10000 + price1000+"000"
    # 거래상태
    status = driver.find_element_by_xpath('//*[@id="slipform"]/div/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[6]/td/table/tbody/tr[2]/td').text
    content = {
        'name':name,
        'price': price,
        'status': status,
    }
    # 창 닫기
    close = driver.close()
    return content