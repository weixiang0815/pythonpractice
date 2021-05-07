from selenium import webdriver
import time
import os

driver = webdriver.Chrome("C:\\Users\\henry\\Desktop\\Python Training\\chromedriver.exe")

driver.get('http://facebook.com')
driver.execute_script("window.open('http://twitter.com', 'new window')")
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.get('http://google.com')
print('Google is opened')

driver.execute_script("window.open('http://yahoo.com', 'new window')")
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.get('http://ask.com')
time.sleep(3)
print('Ask.com is opened')

driver.execute_script("window.open('http://bing.com', 'new window')")
time.sleep(3)
driver.switch_to.window(driver.window_handles[2])
time.sleep(3)
driver.get('http://gmail.com')
time.sleep(3)
print('Gmail is opened')
os.system("taskkill /f /im chromedriver.exe")
