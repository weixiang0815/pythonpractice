from selenium import webdriver
import requests

driver = webdriver.Chrome("C:\\Users\\henry\\Desktop\\Python Training\\chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.find_element_by_id("search").send_keys("python desktop automation\n")
getURL = driver.current_url
req = requests.get(getURL)
print(req.text)
os.system("taskkill /f /im chromedriver.exe")
