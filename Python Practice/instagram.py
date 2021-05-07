from selenium import webdriver
from time import sleep

# 設定使用者偏好將通知顯示授權請求視窗關閉
op = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
op.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=op)

# 進入IG首頁
driver.get('http://instagram.com')
print('歡迎來到IG ~ ~ ~')
sleep(3)

# 輸入使用者資料以登入IG
print('正在登入中......')
driver.find_element_by_name('username').send_keys('weixiang_w\t27092916\n')
print('登入成功 ! ! !')
sleep(3)

# 點擊"稍後再說"按鈕
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
print('已點擊"稍後再說"按鈕')
sleep(3)
os.system("taskkill /f /im chromedriver.exe")
