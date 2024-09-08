from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Initialize the WebDriver (no need for explicit path if it's in the environment PATH)
driver = webdriver.Chrome(options=options)

driver.get('https://www.dailymotion.com/tseries2')

time.sleep(10)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)

video_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/video/')]")
video_urls = [elem.get_attribute('href') for elem in video_elements]

driver.quit()

video_urls = video_urls[:500]

video_ids = [url.split('/video/')[1] for url in video_urls]

# Combine all video IDs into one string
all_video_ids = ''.join(video_ids).lower()

# Print the combined string of all video IDs
print(all_video_ids)
