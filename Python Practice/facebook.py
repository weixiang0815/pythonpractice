from selenium import webdriver

# 設定使用者偏好將通知顯示授權請求視窗關閉
op = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
op.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=op)

# 進入FB首頁並登入
driver.get('https://www.facebook.com/')
print('歡迎來到FB ~ ~ ~')
print('正在登入中......')
driver.find_element_by_id('email').send_keys('henry940129@yahoo.com.tw\thenry880815\n')
print('登入成功 ! ! !')
os.system("taskkill /f /im chromedriver.exe")
