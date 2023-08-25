import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\drivers\chrome\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://toolsqa.com/")

# driver.maximize_window()

# 1. Mouse Hovering Operation

# Clicks the Tutorial
# driver.find_element(By.XPATH,"//span[@class='navbar__tutorial-menu--text']").click()

# Clicks on the Front-End Testing Automation Button
# frontEndTesting = driver.find_element(By.XPATH,"//span[normalize-space()='Front-End Testing Automation']")

# object of ActionChains
# act = ActionChains(driver)

# used to move the mouse to the middle of an element
# act.move_to_element(frontEndTesting).perform()


# 2. Right Click Operation

# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# driver.maximize_window()

# "Right Click Me" Button
# btn = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

# act = ActionChains(driver)

# Right-clicks on the "Right Click Me" Button
# act.context_click(btn).perform()


# 3. Scroll Operation

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 3.1 Specific number of pixel

# Scroll the page by 3000 pixels
driver.execute_script("window.scrollBy(0,3000)", "")
# Get the number of pixels moved
px = driver.execute_script("return window.pageYOffset;")
print("i. The no. of pixels moved: ",px)

# 3.2 Specific element

# Find the element with alt attribute 'Flag of India'
indflag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# Scroll the page to bring the element into view
driver.execute_script("arguments[0].scrollIntoView();", indflag)
# Get the number of pixels moved
px = driver.execute_script("return window.pageYOffset;")
print("ii. The no. of pixels moved for Indian Flag : ", px)

# 3.3 End of the page


driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
px = driver.execute_script("return window.pageYOffset;")
print("iii. The no. of pixels moved to reach END of the Page: ", px)

time.sleep(2)

# 3.4 Beginning of the page

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
px = driver.execute_script("return window.pageYOffset;")
print("iv. The no. of pixels moved to reach BEGINNING of the Page: ", px)



time.sleep(3)