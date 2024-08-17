from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the Expedia website
driver.get("https://www.expedia.com/")

# Wait for the Flights tab and click on it using the provided XPath
flights_tab = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='multi-product-search-form-1']/div/div/div/div/div[1]/ul/li[2]/a/span"))
)
flights_tab.click()

# Add a short delay to ensure the page loads
time.sleep(5)
# 




# 
# Click the Departure City Tab to open the input field
departure_city_tab = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='FlightSearchForm_ROUND_TRIP']/div/div[1]/div/div[1]/div/div/div[2]/div[1]/button"))
)
departure_city_tab.click()

# Automatically enter the departure city
departure_city_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="origin_select"]'))
)
departure_city_input.send_keys("Kolkata")
departure_city_input.send_keys(u'\ue007')  # Press Enter to confirm

# Wait for the Destination City input tab and click on it using the provided XPath
destination_city_tab = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='FlightSearchForm_ROUND_TRIP']/div/div[1]/div/div[2]/div/div/div[2]/div[1]/button"))
)
destination_city_tab.click()

# Automatically enter the destination city
destination_city_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="destination_select"]'))
)
destination_city_input.send_keys("Hyderabad")
destination_city_input.send_keys(u'\ue007')  # Press Enter to confirm

# Wait for the Departure Date Picker and click on it using the provided XPath
departure_date_picker = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="FlightSearchForm_ROUND_TRIP"]/div/div[2]/div/div[1]/div/div/button'))
)
departure_date_picker.click()

# Select the specific date (e.g., 17th September) in the calendar using the provided XPath
september_17th_date = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="u9xlf"]/span'))
)
september_17th_date.click()

# Click the "Done" button using one of the methods mentioned above
apply_date_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="f94mnw"]/span'))
)
# Try JavaScript click if normal click doesn't work
driver.execute_script("arguments[0].click();", apply_date_button)

# Wait for the Travellers Selector and click on it using the provided XPath
travellers_selector = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='FlightSearchForm_ROUND_TRIP']/div/div[3]/div/div[1]/button"))
)
travellers_selector.click()

# Increase the number of adults using the provided XPath
increase_adults = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='FlightSearchForm_ROUND_TRIP']/div/div[3]/div/div[2]/div/div/section/div[1]/div/div/button[2]/span"))
)
increase_adults.click()

# Confirm the selection by clicking the Done button using the provided XPath
done_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='travelers_selector_done_button']"))
)
done_button.click()

# Finally, click the Search button to find available flights using the provided XPath
search_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='search_button']"))
)
search_button.click()

# Wait for the first flight to be selectable and click on it using the provided XPath
first_flight = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='AQqqAgqUAnY1LXNvcy1jYTZiNDQ5M2I2ZDA0NzY5ODJmODcxY2Q1ZmJlNzFhYS0xMjktNTUtNTEyfjIuU35BUW9DQ0FFU0J3alVCQkFCR0FFb0FsSUV1NzhDQUZnQ2NBQjZESFJ5WVhabGJHWjFjMmx2Ym9nQm9Oak9SUX5BUW9zQ2lvSXRvb0JFZ016TXpRWXdxQUJJSWNlS0tpaTFnSXdyNlBXQWpoVFFBQllBWElJVXpFMU1EaEJVRGNLTFFvckNMYUtBUklFTmprd054aUhIaURDb0FFbzVQTFdBakRtODlZQ09GTkFBRmdCY2doVE1UVXdPRUZRTnhJS0NBc1FBUmdJS2dJMlJSZ0NJZ1FJQVJBQ0tBSXdBdxEAAAAAAEBvQCIBASoFEgMKATESRwoaCgoyMDI0LTA4LTMwEgNDQ1UaA0hZRDABOAEKGgoKMjAyNC0wOS0wNhIDSFlEGgNDQ1UwATgBEgcSBUNPQUNIGgIQAiACGggIARIEGgAiAA==']/div/div/button"))
)
first_flight.click()

# Continue with any further steps, such as booking the flight, or close the browser
