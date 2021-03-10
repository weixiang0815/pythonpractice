from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('C:\\Users\\henry\\Desktop\\Python Training\\Python Selenium\\chromedriver.exe')
driver.get('https://www.timeanddate.com/')
driver.maximize_window()

selectElements = driver.find_element_by_id('month')
months = Select(selectElements)
months.select_by_visible_text('December')

countriesElements = driver.find_element_by_id('country')
countries = Select(countriesElements)
countries.select_by_visible_text('Russia')

driver.find_element_by_css_selector('body.tpl-index:nth-child(2) div.main-content-div:nth-child(2) div.fixed:nth-child(3) div.flex-grid div.four.columns.c-cl.med-6:nth-child(3) div.rd-box div.rd-inner form.small:nth-child(3) div.form-row:nth-child(4) > input:nth-child(1)').click()

# 停止chromedriver.exe指令:taskkill /f /im chromedriver.exe
