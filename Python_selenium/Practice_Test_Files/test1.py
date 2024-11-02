import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("--incognito")
ChromeOptions.add_argument("--start-maximized")

driver = webdriver.Chrome(options=ChromeOptions)
namelist= []

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()
carts=driver.find_elements(By.CSS_SELECTOR, ".card.h-100")
for i in carts:
    names = i.find_element(By.TAG_NAME, "h4").text
    if names == "Blackberry":
      namelist.append(names)
      i.find_element(By.CSS_SELECTOR, "button").click()

print(namelist)

driver.find_element(By.CSS_SELECTOR,".nav-item.active").click()
driver.find_element(By.CSS_SELECTOR,"button[class*=btn-success]").click()
driver.find_element(By.CSS_SELECTOR,"input[id='country']").send_keys("ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[text()='India']")))

driver.find_element(By.XPATH,"//a[text()='India']").click()
driver.find_element(By.CSS_SELECTOR,".checkbox.checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()

success_msg = driver.find_element(By.CSS_SELECTOR,"div[class*='alert-success']").text
print(success_msg)
assert "Success! Thank you!" in success_msg

time.sleep(10)