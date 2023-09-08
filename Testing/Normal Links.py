import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

serv_obj=Service("D:\drivers\msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# link text and partial link text
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# find the total number of links
# totallinks=driver.find_elements(By.TAG_NAME,'a')
# print("Total number of links:",len(totallinks))

# find the links using xpath
totallinks=driver.find_elements(By.XPATH,"//a")
print("Total number of links:",len(totallinks))

# print all the link names
for link in totallinks:
    print(link.text)


time.sleep(3)