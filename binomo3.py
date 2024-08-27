from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")

#  Initialize the WebDriver
driver = webdriver.Chrome(options=options)


# Navigate to Binomo
driver.get('https://binomo.com/')

# Wait for the login button to be clickable and then click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="signInBtn"]'))  # Replace with actual XPath
)
login_button.click()

# Locate the email field and enter the email
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="qa_auth_LoginEmailInput"]/way-input/div/div/way-input-text/input'))  # Replace with actual XPath
)
email_field.send_keys('email')

# Locate the password field and enter the password
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="qa_auth_LoginPasswordInput"]/way-input/div/div/way-input-password/input'))  # Replace with actual XPath
)
password_field.send_keys('pass')

# Submit the form
password_field.send_keys(Keys.RETURN)

#  Wait until the trading page loads
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="chart"]/canvas'))  # Ensure the trading page is loaded
)

# Click the "Up" or "Down" button to place an order,here we are taking only up trade
# Replace the XPaths with the correct ones from the actual elements on your page
up_button = driver.find_element(By.XPATH, '//*[@id="qa_trading_dealUpButton"]/button')  # Replace with actual XPath
up_button.click()

# Wait for 40 seconds after placing the order
time.sleep(40)

# Close the browser once done
driver.quit()
