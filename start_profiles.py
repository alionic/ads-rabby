import os

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


ADS_API_URL = os.getenv("ADS_API_URL")

def start_profile(profile_id: str, profile_name: str) -> dict:
	print(f"Open profile {profile_name}...", end = "")
	open_url = f"{ADS_API_URL}/api/v1/browser/start?user_id={profile_id}"
	close_url = f"{ADS_API_URL}/api/v1/browser/stop?user_id={profile_id}"

	resp = requests.get(open_url).json()
	if resp["code"] != 0:
		print("ERROR")
		print(resp["msg"])
		print(f"Please check ads_id of profile {profile_name}")
	else:
		print("OK")
		return resp

def init_driver(resp) -> webdriver.Chrome:
	chrome_driver =resp["data"]["webdriver"]
	options = Options()
	options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
	service = Service(executable_path=chrome_driver)
	driver = webdriver.Chrome(service=service, options=options)
	driver.implicitly_wait(10) 
	return driver