from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()


# Navigate to the Expedia website
driver.get("https://binomo.com/trading")

time.sleep(10)


# //*[@id="qa_auth_LoginEmailInput"]/way-input/div/div[1]/way-input-text/input
# email xpath -- //*[@id="qa_auth_LoginEmailInput"]/way-input/div/div/way-input-text/input
# pass xpath -- //*[@id="qa_auth_LoginPasswordInput"]/way-input/div/div/way-input-password/input


# Click the Departure City Tab to open the input field
departure_city_tab = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="qa_auth_LoginEmailInput"]/way-input/div/div/way-input-text/input'))
)
departure_city_tab.click()

# Automatically enter the departure city
departure_city_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="qa_auth_LoginEmailInput"]/way-input/div/div[1]/way-input-text/input'))
)

departure_city_input.send_keys("sk54")
departure_city_input.send_keys(u'\ue007')  
