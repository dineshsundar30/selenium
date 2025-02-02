import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# Set up WebDriver (e.g., Chrome)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
# Open the target URL
driver.get("https://financialgear.blogspot.com/2024/12/test.html")  # Replace with the actual URL

# Locate the file input field
 # Replace with the actual ID or locator

# Specify the path of the file to be uploaded
file_path = r"C:\\Users\\dkdat\\\Downloads\\test.png"

# Upload the file
file_input = driver.find_element(By.ID, "file-input")

file_input.location_once_scrolled_into_view   #It will scroll into that webelement
time.sleep(5)
file_input.send_keys(file_path)
