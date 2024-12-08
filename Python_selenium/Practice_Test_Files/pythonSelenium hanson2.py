from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# navigating through the page and in grab the each page title

def main3():
    # 1. Give me the count of links on the page.
    # 2. Count of footer section-

    driver = webdriver.Chrome()

    driver.get("http://qaclickacademy.com/practice.php")

    print(len(driver.find_elements(By.TAG_NAME, "a")))

    footerdriver = driver.find_element(By.ID, "gf-BIG")  # Limiting webdriver scope

    print(len(footerdriver.find_elements(By.TAG_NAME, "a")))

    # 3-
    coloumndriver = footerdriver.find_element(By.XPATH, "//table/tbody/tr/td[1]/ul")
    print(len(coloumndriver.find_elements(By.TAG_NAME, "a")))

    # 4- click on each link in the column and check if the pages are opening-
    for i in range(1, len(coloumndriver.find_elements(By.TAG_NAME, "a"))):
        clickonlinkTab = Keys.CONTROL + Keys.ENTER

        coloumndriver.find_elements(By.TAG_NAME, "a")[i].send_keys(clickonlinkTab)
        time.sleep(5)  # Sleep for 5 seconds to allow the new tab to open

    # opens all the tabs
    abc = driver.window_handles  # 4

    for window in abc:
        driver.switch_to.window(window)
        print(driver.title)

    driver.quit()


if __name__ == "__main__":
    main3()

