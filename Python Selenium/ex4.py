from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\henry\\Desktop\\Python Training\\Python Selenium\\chromedriver.exe')
driver.get('https://www.youtube.com/')
driver.maximize_window()
driver.save_screenshot('C:\\Users\\henry\\Desktop\\截圖1.png')
driver.find_element_by_id('search').send_keys('哈囉我叫王威翔~~~')
driver.save_screenshot('C:\\Users\\henry\\Desktop\\截圖2.png')

# 停止chromedriver.exe指令:taskkill /f /im chromedriver.exe
