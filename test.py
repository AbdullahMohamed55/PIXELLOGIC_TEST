from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
PATH = '/home/abdo/Documents/pixellogic/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://www.phptravels.net/register')


firstname = driver.find_element_by_name('firstname')
firstname.send_keys('Abdullah')
lastname = driver. find_element_by_name('lastname')
lastname.send_keys('Abdullah')
phone = driver.find_element_by_name('phone')
phone.send_keys('Abdullah')
email = driver.find_element_by_name('email')
email.send_keys('Abdullah')
password = driver.find_element_by_name('password')
password.send_keys('Abdullah')
confirmpassword = driver.find_element_by_name('confirmpassword')
confirmpassword.send_keys('Abdullah')

signup = driver.find_element_by_class_name('signupbtn')
signup.click()

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"")
        ))
except:
    drivcer.quit()
time.sleep(5)
driver.quit()
"""

driver.clear()
driver.back()
driver.forward()
"""