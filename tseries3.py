from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Counter
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')

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

all_video_ids = ''.join(video_ids).lower()

char_count = Counter(all_video_ids)

most_frequent_char, highest_count = min(char_count.items(), key=lambda x: (-x[1], x[0]))

print(f"{most_frequent_char}:{highest_count}")
