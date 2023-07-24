# P6 : Automation Script to Control the Checkboxes in the Web Page

# Import necessary modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the ChromeDriver service
serv_obj = Service("C:\drivers\chrome\chromedriver.exe")

# Create a new ChromeDriver instance
driver = webdriver.Chrome(service=serv_obj)

# XPATH Axes
# Navigate to the webpage to be scraped
driver.get("https://itera-qa.azurewebsites.net/home/automation")

# Maximize the browser window
driver.maximize_window()

# 1. Selecting/Checking a Single Specific Checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# 2. Selecting/Checking Multiple Checkboxes
# since there are 14 checkboxes in the entire page , we differentiate our 7 checkboxes by
# using contains() with respect to @id containing 'day'
# cannot use click(), due to multiple elements, so we go with len()
daysOfWeek = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print("Total Number of Checkboxes with id containing 'day' : ", len(daysOfWeek))

# For loop to click multiple checkboxes Approach - 1
# for i in range(len(daysOfWeek)):
#     daysOfWeek[i].click()

# For loop to click multiple checkboxes Approach - 2
# for i in daysOfWeek:
#     i.click()


# 3. Selecting Multiple Checkboxes of User Choice [Monday , Sunday]
# for i in daysOfWeek:
#     weekday = i.get_attribute('id')
#     if weekday == 'monday' or weekday == 'sunday':
#         i.click()


# 4. Selecting 2 Checkboxes from Last
# range(5,7)
# for i in range(len(daysOfWeek)-2,len(daysOfWeek)):
#     daysOfWeek[i].click()

# 5. Selecting First 2 Checkboxes
for i in range(len(daysOfWeek)):
    if i < 2:
        daysOfWeek[i].click()
# Adding this to wait before next code is followed [Before Uncheck ]
time.sleep(3)
# 6. Unselecting all the checkboxes
for i in daysOfWeek:
    if i.is_selected():
        i.click()

# Wait for 3 seconds [After we Uncheck ]
time.sleep(3)