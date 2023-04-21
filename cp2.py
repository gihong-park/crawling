# -*- conding: utf-8 -*-
import os, sys, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

from save import save_to_file

from defs import source

co = Options()
co.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver= "C://chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=co)

# current page source
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
# table_num
table = soup.find("table", {"class":"list_table"})
# print(table)
tbody = table.find("tbody")
trs = tbody.find_all("tr")

result=[]
for tr in range(len(trs)):
    data = result.append(source(tr+1))
    driver.switch_to.window(driver.window_handles[0])

print(result)

save_to_file(result)
