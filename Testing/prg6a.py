import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(" https://chromedriver.chromium.org/")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://text-compare.com/")
driver.maximize_window()

# send keys
input_box=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input_box2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input_box.send_keys("welcome to selenium")
input_box2.send_keys("welcome to selenium")
act=ActionChains(driver)

#1 inputbox - ctrl +a - select the text
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

# Alternative
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#copy
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#tab
act.send_keys(Keys.TAB).perform()
#
#paste
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(4)


time.sleep(3)