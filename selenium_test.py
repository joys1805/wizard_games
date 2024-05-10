from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Initialize the WebDriver 
browser = webdriver.Chrome()

# Open the webpage
browser.get("https://www.saucedemo.com")
user1 = "standard_user"
pwd = "secret_sauce"
# Find the username and password fields and input your credentials
user_field = browser.find_element("id","user-name")
user_field.send_keys(user1)

pwd_field = browser.find_element("id","password")
pwd_field.send_keys(pwd)

# Submit the form
pwd_field.send_keys(Keys.RETURN)

# Check if login was successful by verifying a specific element on the page
if "Swag Labs" in browser.page_source:
    print("Login successful")
else:
    print("Login failed!")
browser.save_screenshot("screenshot1.png")
# Close the browser
browser.quit()


# Initialize the WebDriver 
browser = webdriver.Chrome()

# Open the webpage
browser.get("https://www.saucedemo.com")
user1 = "locked_out_user"
pwd = "secret_sauce"
# Find the username and password fields and input your credentials
user_field = browser.find_element("id","user-name")
user_field.send_keys(user1)

pwd_field = browser.find_element("id","password")
pwd_field.send_keys(pwd)

# Submit the form
pwd_field.send_keys(Keys.RETURN)

# Check if login was successful by verifying a specific element on the page
if "Sorry, this user has been locked out" in browser.page_source:
    print("Login failed")
else:
    print("Login success")
browser.save_screenshot("screenshot2.png")
# Close the browser
browser.quit()

# Initialize the WebDriver 
browser = webdriver.Chrome()

# Open the webpage
browser.get("https://www.saucedemo.com")
user1 = "standard_user"
pwd = "secret_sauce"
# Find the username and password fields and input your credentials
user_field = browser.find_element("id","user-name")
user_field.send_keys(user1)

pwd_field = browser.find_element("id","password")
pwd_field.send_keys(pwd)

# Submit the form
pwd_field.send_keys(Keys.RETURN)

sort_dropdown = browser.find_element(By.CLASS_NAME,"product_sort_container")
# sort_dropdown = webdriver.Chrome().fi.find_element_by_css_selector("[data-test='active-options']")

select = Select(sort_dropdown)

select.select_by_value("hilo")

add_cart_field = browser.find_element("id","add-to-cart-sauce-labs-fleece-jacket")

add_cart_field.send_keys(Keys.RETURN)
click_cart = browser.find_element("id","shopping_cart_container")
click_cart.click()
click_checkout = browser.find_element("id","checkout")
click_checkout.click()
firstname = "Alice"
lastname = "Doe"
zipcode = 592
firstname_field = browser.find_element("id","first-name")
firstname_field.send_keys(firstname)

lastname_field = browser.find_element("id","last-name")
lastname_field.send_keys(lastname)

zipcode_field = browser.find_element("id","postal-code")
zipcode_field.send_keys(zipcode)

click_continue = browser.find_element("id","continue")
click_continue.click()

totalAmount_field = browser.find_element(By.CLASS_NAME,"summary_total_label")

if totalAmount_field == 49.99:
    print("The total amount for the added item is $49.99")

else:
    print("The total amount for the added item is not $49.99")
browser.save_screenshot("screenshot3.png")
finish_field = browser.find_element("id","finish")
finish_field.click()
browser.quit()