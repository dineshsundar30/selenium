# Selenium Python – Notes

## Selenium Web Driver Locators

As part of Automation, Selenium performs actions (such as click, typing) on the Page HTML Elements.

The Locators are the way to identify an HTML element on a web page.  
Selenium WebDriver uses any of the below locators to identify the element on the page and performs the Action:

### ID
```python
driver.find_element(By.ID, "inputUsername").send_keys("Dk")
```

### Xpath
```python
driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("John")
```

### CSS Selector
```python
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys("john@rsa.com")
```

### Name
```python
driver.find_element(By.NAME, "inputPassword").send_keys("hello123")
```

### Class Name
In class name if we have spaces you can use anyone or replace the spaces with.
```python
driver.find_element(By.CLASS_NAME, "signInBtn").click()
```

### Tag Name
```python
print(driver.find_element(By.TAG_NAME, "p").text)
```

### Link Text
```python
driver.find_element(By.LINK_TEXT, "Forgot your password?").click()
```

### Partial Link Text
```python
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
```

```html
<input class="form-control ng-pristine ng-invalid ng-touched" minlength="2" name="name" required="" type="text">
```

Input -> tag name.  
Red -> attribute.  
Green -> attribute associated value.

### Example for combination of selectors (xpath, indexing, parent to child)
```python
driver.find_element(By.XPATH, "//div[@class='forgot-pwd-btn-conainer']/button[1]").click()
```

## CSS Selector Details

### Class name
```python
# tagname.classname
print(driver.find_element(By.CSS_SELECTOR, "p.error").text)
```

### ID
```python
# tagname#id -> input#inputUsername
driver.find_element(By.CSS_SELECTOR, "#inputUsername").send_keys("Dinesh")
```

### Attribute value
```python
# Tagname[attribute='value']
# <input type="text" placeholder="Username" value=" ">
# Input[placeholder='Username']
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys("john@rsa.com")
```

### Child items
```python
# Tagname[@attribute='value']:nth-child(index)
driver.find_element(By.CSS_SELECTOR, "input[type='text']:nth-child(3)").send_keys("john@gmail.com")
```

### Parent Tag to Child Tag
```python
print(driver.find_element(By.CSS_SELECTOR, "div[id='content'] div h3").text)
```

### Parent tag to child tag using spaces
```python
# Parenttagname childtagname
print(driver.find_element(By.CSS_SELECTOR, "form p").text)
# Here we can get the selector based on the parent to child tags using parent tag and child tag like parenttag space childtag
```

### Partial attribute value
```python
# input[type*='pass']
# If we use * it will scan all the partial value like that you passed inside the single quotes
# If you see space between the class name it's 2 class names, you can take one class name or remove space between class names and replace with a dot
driver.find_element(By.CSS_SELECTOR, "input[type*='pass']").send_keys("rahulshettyacademy")
```

### Class selector shorthand
```python
# .classname
driver.find_element(By.CSS_SELECTOR, ".reset-pwd-btn").click()
```

### Tag name selector
```python
print(driver.find_element(By.TAG_NAME, "p").text)
```

### Image based CSS
```python
driver.find_element(By.CSS_SELECTOR, "a[href*='windows']").click()
# For example if you seen this kind of image you can use like above one href="/windows/new"
```

## Xpath Details

### Basic syntax
```python
# //Tagname[@attribute='value']
# //input[@placeholder='Username']
driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("John")
# <input type="text" placeholder="Name">
# //input[@placeholder='Name']
```

### Using index
```python
# //Tagname[@attribute='value'][index]
driver.find_element(By.XPATH, "//input[@type='text'][2]").clear()
```

### Parent to child
```python
# //parentTagname/childTagname
print(driver.find_element(By.XPATH, "//div[@id='content']/div/h3").text)
```

### Using contains (Regular expression)
```python
# //button[contains(@class,'submit')]
driver.find_element(By.XPATH, "//button[contains(@class,'submit')]").click()
# To scan with the partial value in xpath
```

### Sibling traversal
```python
# //header/div/button[1]/following-sibling::button[1]
print(driver.find_element(By.XPATH, "//header/div/button[1]/following-sibling::button[1]").text)
# Moving parent to child
```

### Parent traversal
```python
# //header/div/button[1]/parent::div
print(driver.find_element(By.XPATH, "//header/div/button[1]/parent::div/button[2]").text)
# Moving child to parent
```

### Find by text
```python
# To find locators based on text
driver.find_element(By.XPATH, "//*[text()='Female']").click()
# Here the * will scan all tags in that page
```

### Scan all tags
```python
driver.find_element(By.XPATH, "//*[text()='Log Out']").click()
# We can find selectors using text in page using this xpath //tagname or *(it scans all tags with the name)[text()='text in that page']
```

### Parent to child alternative
```python
# Parent to child
driver.find_elements(By.XPATH, "//div[@class='product-action']/button")[i].click()
# This is one fine way to go from parent to child
```

### Nested parent-child selection
```python
driver.find_element(By.XPATH, "//div[@id='glsctl00_mainContent_ddl_destinationStation1_CTNR'] //a[@value='PNQ']").click()
```

## Important Note for Python Selenium

In Python Selenium, we import the By class from selenium.webdriver.common.by module:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize driver
driver = webdriver.Chrome()  # or Firefox, Edge, etc.
```

Also, note that in Python Selenium:
- `findElement` becomes `find_element`
- `findElements` becomes `find_elements`
- `getText()` becomes `.text`
- `click()` becomes `.click()`
- `sendKeys()` becomes `.send_keys()`
