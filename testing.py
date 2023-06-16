from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()  # Change this to the appropriate WebDriver for your browser

# Navigate to the login page
driver.get("https://gmail.com")  # Replace with the actual login page URL

# Find the username and password input fields and enter the credentials
username_field = driver.find_element(By.ID, "praveenvbce")  # Replace "username" with the actual ID of the username input field
password_field = driver.find_element(By.ID, "Krishna@!4")  # Replace "password" with the actual ID of the password input field

username_field.send_keys("your_username")  # Replace "your_username" with the actual username
password_field.send_keys("your_password")  # Replace "your_password" with the actual password

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load or for a specific element to appear (if necessary)
# You can use driver.implicitly_wait(10) to wait for 10 seconds implicitly

# Perform the validation
expected_title = "Home Page"  # Replace "Home Page" with the expected title of the logged-in page
actual_title = driver.title

if expected_title in actual_title:
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser
driver.quit()