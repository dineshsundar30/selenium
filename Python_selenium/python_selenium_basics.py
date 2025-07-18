#Browser Setup
#browser basics browser actions

from selenium import webdriver
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome()
#driver=webdriver.Firefox()
driver = webdriver.Ie() # or we can use this driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")  #get method to hit url on  browser

     
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close(), driver.quit()       #In Selenium, driver.close() closes the current browser window, while driver.quit() 
                                                       #closes all browser windows and ends the WebDriver session


#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#Selecting dropdown 
from selenium import webdriver
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul")
driver.find_element(By.NAME,"email").send_keys("Shetty")

driver.find_element(By.ID,"exampleCheck1").click()

#select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.XPATH,"//input[@type='submit']").click()

message = driver.find_element(By.NAME,"alert-success").text

assert "success" in message
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#selecting the city from the dropdown
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.find_element(By.ID,"fromCity").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='From']").send_keys("del")
time.sleep(2)
cities =driver.find_elements(By.CSS_SELECTOR,"p[class*='blackText']")
print (len(cities))
for city in cities:
    if city.text =="Del Rio, United States":
        city.click()
        break


driver.find_element(By.XPATH,"//p[text()='Delhi, India']").click()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# alerts
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
name = "dk"
driver = webdriver.Chrome()
driver.get("http://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Your Name']").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "input[value='Alert']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#alert.dismiss()
assert name in alert.text
time.sleep(1)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#checkboxes

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_element(By.NAME,"radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


assert driver.find_element(By.ID,"displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

assert not driver.find_element(By.ID,"displayed-text").is_displayed()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#Implicit wait  -
#Explicit Wait

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# wait until 5 seconds if object is not displayed
#Global wait
#1.5 second to reach next page- execution will resume in 1.5 seconds
#if object do not show up at all, then max time your test waits for 5 seconds
driver = webdriver.Chrome()
driver.get("http://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)          #Implicit wait  -
driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("ber")
cart = driver.find_elements(By.XPATH, "//div[@class='product']")
assert len(cart)>0
Product_List = []
for i in cart:
    i.find_element(By.TAG_NAME,"button").click()
    Product_List.append(i.find_element(By.XPATH,"h4[@class='product-name']").text)
print(Product_List)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait = WebDriverWait(driver,10)   #Explicit Wait  we need to import Explicit Wait and pected_conditions here
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

'''   fluent waits

# Wait 10 seconds, check every 1 second
wait = WebDriverWait(driver, 10, poll_frequency=1,ignored_exceptions=[NoSuchElementException])
wait.until(EC.presence_of_element_located((By.ID, "my-element-id")))

'''

check1 = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(check1)
discountAmt = driver.find_element(By.XPATH,"//span[@class='discountAmt']").text
totAmt = driver.find_element(By.XPATH, "//span[@class='totAmt']").text
assert discountAmt<totAmt
time.sleep(5)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#actions

action = ActionChains(driver)
#action.double_click(driver.find_element(By.))   
#action.context_click().perform()     #righ click
#action.drag_and_drop().perform() 
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# windows switching

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service("/Users/rahulshetty/documents/geckodriver")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

#----------------------------------------------------------------------------------------------------------------------------------------------------------

#iframe
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame(driver.find_element(By.ID,"example-frame"))
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content()  #switching to default content  is importent to print out side ferm once it's called
print(driver.find_element(By.CSS_SELECTOR,"h3").text)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#scrolling using javascript obj and ChormeOptions for like  headless mode

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.addArguments("--incognito")
chrome_options.addArguments("--start-maximized")

service_obj = Service("/Users/rahulshetty/documents/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

------------------screenshot -----------
driver.get_screenshot_as_file("screen.png")

# Locate the element you want to capture
element = driver.find_element(By.ID, "my-element-id")

# Save the screenshot of the element
element.screenshot("element_screenshot.png")

| Method                                      | Purpose                            | Example                                      |
| ------------------------------------------- | ---------------------------------- | -------------------------------------------- |
| `driver.get_screenshot_as_file("file.png")` | Full browser window                | ✅                                            |
| `driver.get_screenshot_as_png()`            | Returns image bytes of full screen | `img_bytes = driver.get_screenshot_as_png()` |
| `element.screenshot("file.png")`            | Screenshot of specific element     | ✅ Recommended for single UI parts            |


#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Sorting Tables

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browserSortedVeggies =[]
service_obj = Service("/Users/rahulshetty/documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect all veggie names -> BrowserSortedveggieList ( A,B, C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# Sort this BrowserSortedveggieList => newSortedList -> (A,B,C)
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList




#--------------------------------------------------------------------------------------------------------------------------------------------------------

