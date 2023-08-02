import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click()
#selecting month in drop down date picker
datepicker_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text("Dec")

#selecting year in drop down date picker
datepicker_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
datepicker_year.select_by_visible_text("2020")

#selecting date from date picker drop down
alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in alldates:
    if date.text=="25":
        date.click()
        break
time.sleep(3)