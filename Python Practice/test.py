from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome('C:\\Users\\henry\\Desktop\\Python Training\\chromedriver.exe')
urllist = []

driver.get('https://cool.ntu.edu.tw/')
driver.minimize_window()
driver.find_element_by_link_text('以計中帳號登入').click()
driver.find_element_by_name('ctl00$ContentPlaceHolder1$UsernameTextBox').send_keys('b07302229\tHenry880815\n')
sleep(1)
driver.get('https://cool.ntu.edu.tw/courses/5487/assignments/35300')
anonymous = driver.find_elements_by_link_text('匿名使用者')
n = 1
for i in anonymous:
    urllist += [i.get_attribute('href')]
n = 1
for i in urllist:
    print('第' + str(n) + '個:')
    # driver.get(i)
    req = requests.get(i).content
    myParser = BeautifulSoup(req, 'html.parser')
    print(myParser.prettify())
    # texts = myParser.findAll('h2', 'h1', 'h3')
    # for x in texts:
    #     print(x.string)
    print('\n' * 3)
    print('-' * 100)
    n += 1
