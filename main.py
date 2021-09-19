# Github automater by HermanCCC
import selenium
import github
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
url = 'https://github.com/new'
browser.get(url)

# Login
browser.find_element_by_id('login_field').send_keys('Your Username')
time.sleep(1)
browser.find_element_by_id('password').send_keys('Your password')
browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()

# Repository options
browser.find_element_by_id('repository_name').send_keys('New repo')
browser.find_element_by_id('repository_description').send_keys('This is a lame description, replace it.')
browser.find_element_by_xpath('//*[@id="repository_auto_init"]').click()
browser.find_element_by_xpath('//*[@id="repository_gitignore_template_toggle"]').click()
browser.find_element_by_xpath('//*[@id="repository_visibility_private"]').click()

# confirm
print('Complete')
