import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

#1.selecting a date picker
driver.switch_to.frame(0)
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("12/10/2022")


#2. Date checking (future dates)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
year="2024"
month="May"
date="11"

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon==month and year==yr:
        break
    else:
        #checking dates of future years
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        #selecting the dates of previous years
        # driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

# 3. Select Multiple all the dates and click on what is assigned above
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text==date:
        ele.click()
        break
time.sleep(2)
