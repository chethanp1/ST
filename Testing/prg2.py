import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("")

# Set up the ChromeDriver service
serv_obj = Service("C:\drivers\chrome\chromedriver.exe")

# Create a new ChromeDriver instance
driver = webdriver.Chrome(service=serv_obj)

# XPATH Axes
# Navigate to the webpage to be scraped
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# Maximize the browser window
driver.maximize_window()

# SELF NODE : <a>
# Find the anchor element with the text "Zomato" and extract its text content
# The XPath expression uses the self::a syntax to choose the anchor element as the context node
# .text attribute is used to extract the text content of the element, choosing Zomato as Self Node
# Syntax : /AxisName::ElementName
selfNodeText = driver.find_element(By.XPATH, "//a[contains(text(),'Zomato')]/self::a").text
# Print the extracted text content
print("Inner Text of Self Node <a> \t : \t", selfNodeText)

# # PARENT NODE : <tr>
# parentNodeText = driver.find_element(By.XPATH, "//a[contains(text(),'Zomato')]/parent::td").text
#
# print("Inner Text of Parent Node <td> \t : \t", parentNodeText)
# #
# # ANCESTOR NODE : <tr>
# ancestorNodeText = driver.find_element(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr").text
# print("Inner Text of Ancestor Node <tr> : \t", ancestorNodeText)
#
# # CHILD NODE : <a> doesn't have any child node , so we use ancestor of self node and retrieve the child node i,e <tr>
# # since there are 5 matching elements we make use of find_elements() and
# childNode = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr//child::td")
# print("No. of Child Nodes of Ancestor <tr> \t\t: \t", len(childNode))
#
# # DESCENDANT NODE:<a> doesn't have any child node , so we use ancestor of self node and retrieve the descendant node
# # we use * as we don't know how many descendants exists
# descendantNode = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr//descendant::*")
# print("No. of Descendant Nodes of Ancestor <tr> \t: \t", len(descendantNode))
#
# # following contains all the elements after ancestor (Zomato)
# following = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr//following::*")
# print("No. of Following of ancestor <tr> \t\t\t: \t", len(following))
#
# # following-siblings are only rows
# followingSibling = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr//following-sibling::*")
# print("No. of Following-Sibling of ancestor <tr> \t: \t", len(followingSibling))
#
# # preceding contains all the elements before ancestor (Zomato)
# preceding = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr//preceding::*")
# print("No. of Preceding of ancestor <tr> \t\t\t: \t", len(preceding))
#
# # preceding-siblings are only rows
# precedingSibling = driver.find_elements(By.XPATH, "//a[contains(text(),'Zomato')]/ancestor::tr//preceding-sibling::*")
# print("No. of Preceding-Sibling of ancestor <tr> \t: \t", len(precedingSibling))
#
# # Wait for 3 seconds
time.sleep(5)