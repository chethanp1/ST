import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

serv_obj=Service("D:\drivers\msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks=driver.find_elements(By.TAG_NAME,'a')
count=0
for link in alllinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url," it is a broken link")
        count+=1
    else:
        print(url," is a valid link")
print("Total no. of broken links:",count)

time.sleep(3)