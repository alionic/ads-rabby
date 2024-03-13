import os

from selenium import webdriver
from selenium.webdriver.common.by import By


EXTENSION_ID = os.getenv("EXTENSION_ID")
EXTENSION_URL = f"chrome-extension://{EXTENSION_ID}/index.html"
PASSWORD = os.getenv("PASSWORD")

def rabby_login(driver: webdriver.Chrome, profile_name: str):
	driver.get(EXTENSION_URL)
	driver.refresh()
	print(f"Login {profile_name}...", end = "")
	try:
		driver.find_element(By.XPATH, value='//*[@id="password"]').send_keys(PASSWORD)
		driver.find_element(By.XPATH, value='//*[@id="root"]/div/form/div[2]/div/div/div/button').click()
	except Exception as e:
		print("ERROR")
		print(e)
	driver.quit()
	print("OK")