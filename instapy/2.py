from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:\\Users\\henry\\Desktop\\Python Training\\chromedriver.exe")
driver.get("https://www.instagram.com/")
driver.maximize_window()
sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('weixiang_w\t27092916\n')
sleep(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="f3af099fafcfab8"]/div/div').click()
