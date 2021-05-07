from selenium import webdriver
# import time

driver = webdriver.Chrome("C:\\Users\\henry\\Desktop\\Python Training\\Python Selenium\\chromedriver.exe")

# driver.get('https://www.amazon.com/')
# driver.maximize_window()
# driver.find_element_by_id('nav-link-accountList-nav-line-1').click()
# driver.find_element_by_id('ap_email').send_keys('henry940129@gmail.com\n')
# driver.find_element_by_id('ap_password').send_keys('Henry880815\n')

# driver.get('https://www.google.com/')
# driver.maximize_window()
# driver.find_element_by_link_text('Gmail').click()
# driver.back()
# driver.find_element_by_partial_link_text('mail').click()
# driver.find_element_by_xpath("//a[contains(text(),'Gmail')]").click()
#
# elements = driver.find_elements_by_tag_name('a')
# for element in elements:
#     if 'Gmail' in element.text:
#         element.click()
#
# driver.get('https://www.wealthyaffiliate.com/')
# driver.maximize_window()
# driver.find_element_by_class_name('btn btn-primary btn-login ghost').click()
# # 用class name可能會有重覆性問題
# driver.find_element_by_partial_link_text('Login').click()
# driver.find_element_by_name('email').send_keys('henry940129@gmail.com\t27092916\n')
#
# driver.get('https://www.youtube.com/')
# driver.maximize_window()
# driver.find_element_by_css_selector('#search').send_keys('blender sci fi animation\n')

# time.sleep(10)
# driver.quit()
# 停止chromedriver.exe指令:taskkill /f /im chromedriver.exe
