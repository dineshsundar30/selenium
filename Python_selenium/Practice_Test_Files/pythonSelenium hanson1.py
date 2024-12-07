from selenium import webdriver
import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://financialgear.blogspot.com/2024/12/test.html")
driver.implicitly_wait(20)
driver.execute_script("window.scroll(0,600);")
name = "Dk"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.XPATH,"//*[text()='Submit']").click()

check =  driver.find_element(By.ID,"name-display").text
print("from UI: "+check)
check2 = "Hello, "+name+"!"
print("for assert: "+check2)
assert check == check2
print("Aswm assert pass")

# raido buttoon
driver.find_element(By.CSS_SELECTOR,"input[value='male']").click()
print(driver.find_element(By.CSS_SELECTOR,"p[id='radio-result']").text)


#Buttons
driver.execute_script("window.scroll(0,1000);")
driver.find_element(By.XPATH,"//button[@id='button2']").click()
print(driver.find_element(By.XPATH,"//p[@id='button-click-result']").text)

#drop down
driver.execute_script("window.scroll(0,1500);")
dropdown = Select(driver.find_element(By.ID,"dropdown"))
dropdown.select_by_value("option3")
#print(driver.find_element(By.ID,"dropdown").text)


#drag and drop
driver.execute_script("window.scroll(0,2000);")
ac = ActionChains(driver)
sc = driver.find_element(By.XPATH,"//div[@draggable='true']")
dc = driver.find_element(By.XPATH,"//div[@id='droppable']")
ac.drag_and_drop(sc,dc).perform()
print(driver.find_element(By.CSS_SELECTOR,"p[id='drag-result']").text)



# to count the rows
print("Rows count: "+str(len(driver.find_elements(By.XPATH,"//div/table/tbody/tr/td[1]"))))
print("columns count: "+str(len(driver.find_elements(By.XPATH,"//div/table/thead/tr/th"))))
time.sleep(1)

#alert
driver.execute_script("window.scroll(0,2400);")
driver.find_element(By.ID,"alert-button").click()
time.sleep(1)
alert = driver.switch_to.alert
time.sleep(1)
alert.accept()

#Iframe
driver.execute_script("window.scroll(0,2600);")
time.sleep(1)
driver.switch_to.frame(driver.find_element(By.ID,"example-frame"))
driver.execute_script("window.scroll(0,600);")
time.sleep(1)
driver.switch_to.default_content()


#hidden message
time.sleep(1)
driver.execute_script("window.scroll(0,2900);")
driver.find_element(By.ID,"show-hidden").click()
print(driver.find_element(By.ID,"hidden-message").text)

time.sleep(5)