import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\henry\\Desktop\\Python Training\\chromedriver.exe")
driver.get("https://google.com/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("keyword research\n")
