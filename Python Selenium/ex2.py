from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\\henry\\Desktop\\Python Training\\Python Selenium\\chromedriver.exe')
driver.get('https://www.ntu.edu.tw/')
driver.maximize_window()

getTitle = driver.title
for x in range(10):
    print(getTitle)

driver.get('https://www.amazon.com/')
getURL = driver.current_url
for x in range(5):
    print(getTitle + "　" + getURL)
    driver.refresh()
    print('I\'ve refreshed for the ' + str(x+1) + 'th times')

driver.back()
print('已回到上一頁')
driver.forward()
print('已來到下一頁')

pageSource = driver.page_source
print(pageSource)

time.sleep(10)
driver.quit()

# 停止chromedriver.exe指令:taskkill /f /im chromedriver.exe
