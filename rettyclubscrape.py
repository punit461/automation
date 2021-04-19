from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time



username = 'Enter the username' # Enter the username
password = 'Enter the password' # Enter the password
driver = webdriver.Chrome('C:\link\chromedriver')
URL = 'https://apps.retty-apps.com/parity/tran'
driver.get(URL)
driver.implicitly_wait(100)
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div/input').send_keys(password)
driver.find_element_by_class_name('button-btn').click()
time.sleep(10)


#class_name = 'conten__aneven' or 'content__anodd'
class_name = 'container'



try:

        container = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        for value in container:
            number = value.text
            print(number)
            
            

finally:
    driver.quit()
