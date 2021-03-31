from selenium import webdriver
from time import sleep

email = 'henry940129@gmail.com'
password = '27092916'

driver = webdriver.Chrome()
driver.get('http://my.wealthyaffiliate.com')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="main-tag"]/div/div/div/div/div/div/div[2]/div[2]/div[4]/div[2]/div/input')\
    .send_keys(email+'\t'+password+'\n')
sleep(5)
