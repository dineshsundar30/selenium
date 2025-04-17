import json
import pickle
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from datetime import datetime, timedelta


#user_data = r'C:\Users\dkdat\AppData\Local\Google\Chrome\User Data'
ChromeOptions = webdriver.ChromeOptions()
#ChromeOptions.add_argument("--incognito")
ChromeOptions.add_argument(r'user-data-dir=C:\Users\dkdat\AppData\Local\Google\Chrome\User Data')
ChromeOptions.add_argument(r'--profile-directory=Default')

# Add these options to prevent crashes
ChromeOptions.add_argument("--no-sandbox")
ChromeOptions.add_argument("--disable-dev-shm-usage")
ChromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
ChromeOptions.add_experimental_option("useAutomationExtension", False)
ChromeOptions.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=ChromeOptions)
driver.implicitly_wait(10)
wait = WebDriverWait(driver,15)
action = ActionChains(driver)

#driver.get("https://support.pega.com/")

driver.get("https://msp.pega.com")
driver.switch_to.frame(driver.find_element(By.ID,"PegaGadget0Ifr"))

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"a[name='PDCWidget_pyDisplayHarness_8']")))

PegaDiagnosticCenter = driver.find_element(By.CSS_SELECTOR,"a[name='PDCWidget_pyDisplayHarness_8']")
PegaDiagnosticCenter.location_once_scrolled_into_view
PegaDiagnosticCenter.click()


windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

def get_weekday_yesterday():
    # Get today's date
    today = datetime.today()

    # If today is Saturday (5) or Sunday (6), adjust to Friday (4)
    if today.weekday() == 5:  # Saturday
        yesterday = today - timedelta(days=1)  # Go back 1 day to Friday
    elif today.weekday() == 6:  # Sunday
        yesterday = today - timedelta(days=2)  # Go back 2 days to Friday
    else:
        yesterday = today - timedelta(days=1)  # For weekdays, just go back 1 day

    # Return only the day part of the date
    return yesterday.day


for i in range(0, len(driver.find_elements(By.XPATH, "//td/a"))):
    clickonlinkTab = Keys.CONTROL + Keys.ENTER
    driver.find_elements(By.XPATH, "//td/a")[i].send_keys(clickonlinkTab)
    windowsOpenedlink = driver.window_handles
    print(windowsOpened)
    driver.switch_to.window(windowsOpenedlink[3])
    time.sleep(2)

    try:
        driver.find_element(By.XPATH,"//*[text()='System Resources']").is_enabled()
        time.sleep(1)
        driver.find_element(By.XPATH, "// *[text() = 'Resource Utilization']").click()
        time.sleep(1)

    except:
        driver.find_element(By.XPATH, "// *[text() = 'Resource Utilization']").click()
        time.sleep(1)
    driver.execute_script("document.body.style.zoom = '1'")
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.ID, "PegaGadget1Ifr"))
    selectele = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "select[id='69c2f8b5']")))
    selectele.click()
    Custom_time = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "option[value='Custom']")))
    Custom_time.click()

    #for select the last business day
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"img[name='CalendarImg-1daa7b94']").click()
    time.sleep(1)
    yesterday_date = get_weekday_yesterday()
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a[data-day='" + str(yesterday_date) + "']")))
    driver.find_element(By.CSS_SELECTOR,"a[data-day='" + str(yesterday_date) + "']").click()
    #for hour
    driver.find_element(By.CSS_SELECTOR,"img[name='CalendarImg-1daa7b94']").click()
    time.sleep(1)
    #driver.find_element(By.CSS_SELECTOR,"input[aria-label='hour']").clear()
    driver.find_element(By.CSS_SELECTOR, "input[aria-label='hour']").send_keys("1")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"button[title='Filter/Refresh']").click()
    
    break




   # screenshotpage = driver.find_element(By.CSS_SELECTOR,"div[node_name='ResourceBodySection']")



'''
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"(//span[@class='c-bolt-page-header__nav-link__content'])[85]")))
action.move_to_element(driver.find_element(By.XPATH,"(//span[@class='c-bolt-page-header__nav-link__content'])[85]")).perform()





#navigating to the login
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"(//span[@class='c-bolt-page-header__nav-link__content__signifier c-bolt-page-header__nav-link__content__signifier--only'])[1]")))
action.move_to_element(driver.find_element(By.XPATH,"(//span[@class='c-bolt-page-header__nav-link__content__signifier c-bolt-page-header__nav-link__content__signifier--only'])[1]")).perform()

time.sleep(1)
#clicking the login
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"(//*[text()='Log in'])[2]")))
driver.find_element(By.XPATH,"(//*[text()='Log in'])[2]").click()
time.sleep(1)
driver.find_element(By.ID,"input28").send_keys("nadish.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[class='button button-primary']").click()

#user and password
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@type='password']")))
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("1234!")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"div[class='o-form-button-bar']").click()

'''


