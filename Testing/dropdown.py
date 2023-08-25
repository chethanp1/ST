import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()

dropelement=driver.find_element(By.XPATH,"//select[@id='oldSelectMenu']")
dropcolor=Select(dropelement)

##1. Select option from dropdown
# dropcolor.select_by_visible_text("Red") #this is most widely used option

##2.Select by value
# dropcolor.select_by_value("4")

##3.Select from index
# dropcolor.select_by_index("10")

#4.Capture all options
alloptions=dropcolor.options
print("No of colors in dropdown",len(alloptions))

## 5.Print all options
for opt in alloptions:
    print(opt.text)

##6. without using built-in functions
for opt in alloptions:
    if opt.text=="Yellow":
        opt.click()
        break










time.sleep(2)

